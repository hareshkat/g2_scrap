# Scrap G2 Crowd data

Python script to scrap the company’s details from G2 Crowd URLs provided in a CSV file. We aim to extract information from each website using Playwright, an automation tool for web browsers. The scraped data will be stored in new CSV and JSON files.

To accomplish this, we have used several packages:
1. asyncio: This package provides an event loop for asynchronous programming. It allows us to write asynchronous code using coroutines and async/await syntax.
2. playwright: Playwright is a powerful library for automating web browsers. It allows us to navigate to web pages, interact with elements, and extract data using its high-level API.
3. aiohttp: This package is used to make asynchronous HTTP requests. We use it to call the ZenRows API and fetch the HTML content of the websites we want to scrape.
4. ZenRows API

ZenRows is a tool that simplifies web scraping by handling challenges such as rotating proxies, headless browsers, and CAPTCHAs. It helps bypass anti-bot systems and blocking measures implemented by websites, allowing us to easily collect content from any website with a simple API call. With ZenRows, we can focus on extracting the desired information without worrying about the technical complexities of scraping and bypassing security measures.


## Installation and Configuration
To install and use this project, please follow the steps below:

1. Clone the project by running the following command in your terminal:
   ```
   git clone https://github.com/hareshkat/g2_scrap.git
   ```
3. Navigate to the project's directory structure by running:
   ```
   cd g2_scrap
   ```
4. Set up and configure the virtual environment in the project directory:
   - Open your terminal and run the command:
   ```
   python3 -m venv .venv
   ```
   - Activate the virtual environment by running:
   ```
   source .venv/bin/activate
   ```
5. Install the required dependencies by running the command:
   ```
   pip install -r requirements.txt
   ```
6. Get an API key from ZenRows by creating a free account at https://www.zenrows.com
7. Use this ZenRows API key in the scrap.py file

## Execution
1. After installing all the dependencies, execute
   ```
   python3 scrap.py
   ```
2. This will get the URLs from the `g2crowd_urls.csv` file and start scrapping them one by one.
3. After scrapping each URL, It will create the output files for storing the scrapped data in JSON and CSV format with the file name `scraped_data.json` and `scraped_data.csv`.
4. You can take reference of the sample files attached in this repository `g2crowd_urls.csv, scraped_data.json, scraped_data.csv`.
