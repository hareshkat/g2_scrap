import csv
import json

import aiohttp
import asyncio
from playwright.async_api import async_playwright
import requests
from zenrows import ZenRowsClient


# zenrows API KEY
apikey = 'API_KEY'

# API params 
params = {
    "url": "url",
    "apikey": apikey,
    "js_render": "true",
    "premium_proxy": "true"
}

async def get_selector_text(page, selector):
    """
    This function is to find the selector and return the text content
    :param page: site content object
    :param selector: selector string
    """
    try:
        # Wait for the selector
        element = await page.wait_for_selector(selector)
    except Exception as er:
        # Selector not found on the page.
        print("Selector not found on the page.")
        element = None
    if element:
        return await element.text_content()
    else:
        return ""

async def scrape_g2_url(session, url):
    """
    This function is to get the site data and then using 
    selector query to get the required content.
    :param session: aiohttp client session
    :param url: site url
    """
    params['url'] = url
    async with session.get('https://api.zenrows.com/v1/', params=params) as response:
            g2_data = await response.text()
            print(g2_data[:1000])

            async with async_playwright() as playwright:
                product_details = {}
                product_details['url'] = url
                browser = await playwright.chromium.launch()
                context = await browser.new_context()
                page = await context.new_page()

                await page.set_content(g2_data)

                # Wait for the content to load
                await page.wait_for_load_state()

                pageTitle = await page.title()
                product_details['page_title'] = pageTitle

                # Perform scraping operations using Playwright
                div_selector = 'div.product-head__title div[itemprop="name"]'
                product_details['product_name'] = \
                    await get_selector_text(page, div_selector)

                div_selector = 'div[itemprop="description"]'
                product_details[
                    'product_description'] = \
                    await get_selector_text(page, div_selector)


                user_review = []
                try:
                    div_selector = 'div[data-equalizer="measure-title"]'
                    user_review_parent_ele = await page.wait_for_selector(
                        div_selector)
                    inner_divs_selector = 'div.grid-x'
                    inner_divs = await user_review_parent_ele.query_selector_all(
                        inner_divs_selector)

                    user_review = []
                    for inner_div in inner_divs:
                        review_ele = await inner_div.query_selector(
                            'div.charts--doughnut__reviews')
                        review_title_ele = await inner_div.query_selector(
                            'div[data-equalizer-watch="measure-title"]')
                        if review_ele and review_title_ele:
                            user_review.append({
                                "heading": await review_title_ele.text_content(),
                                "rating": await review_ele.text_content()
                            })
                except Exception as er:
                    print(str(er))

                product_details['user_reviews'] = user_review

                # Close the browser & clean up resources
                await browser.close()
                return product_details

async def save_data_to_json(data, file_name):
    """
    This function is to save scrap data into json file.
    :param data: scrap data
    :param file_name: file name
    """
    with open(file_name, 'w') as outfile:
        json.dump(data, outfile, indent=4)

async def save_data_to_csv(data, file_name):
    """
    This function is to save scrap data into CSV file.
    :param data: scrap data
    :param file_name: file name
    """
    keys = data[0].keys()
    with open(file_name, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

async def main(file_path):
    """
    This function is Main function. It will create async tasks.
    :param file_path: CSV file path contains the urls that needs to be scrap
    """
    # Read the CSV file
    scraped_data = []
    async with aiohttp.ClientSession() as session:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row

            # Create coroutine tasks
            tasks = []
            for row in reader:
                url = row[0]
                tasks.append(asyncio.ensure_future(scrape_g2_url(
                    session, url)))

            # Wait for all tasks to complete
            scraped_data = await asyncio.gather(*tasks)

    if scraped_data:
        # Save the scraped data to JSON
        await save_data_to_json(scraped_data, 'scraped_data.json')

        # Save the scraped data to CSV
        await save_data_to_csv(scraped_data, 'scraped_data.csv')

# Start an asyncio program by creating an event loop
asyncio.run(main('g2crowd_urls.csv'))
