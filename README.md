# Scrap G2 Crowd site data

Python script to scrap the company’s details from G2 Crowd URLs provided in a CSV file. We aim to extract information from each website using Playwright, an automation tool for web browsers. The scraped data will be stored in new CSV and JSON files.

To accomplish this, we have used several packages:
1. asyncio: This package provides an event loop for asynchronous programming. It allows us to write asynchronous code using coroutines and async/await syntax.
2. playwright: Playwright is a powerful library for automating web browsers. It allows us to navigate to web pages, interact with elements, and extract data using its high-level API.
3. aiohttp: This package is used to make asynchronous HTTP requests. We use it to call the ZenRows API and fetch the HTML content of the websites we want to scrape.

We chose Playwright because it provides a user-friendly and efficient way to automate web browsers, making it suitable for web scraping tasks. The combination of asyncio, Playwright, and ZenRows allows us to perform asynchronous operations, enabling concurrent scraping of multiple URLs for improved efficiency.

The csv package simplifies reading and writing data in CSV format, which is a common choice for storing tabular data. By utilizing the csv package, we can handle the input and output of data in a structured and standardized format.

Additionally, the aiohttp package helps us make asynchronous HTTP requests to fetch the HTML content of the websites. We utilize it to retrieve the website content from the ZenRows API asynchronously before passing it to Playwright for further processing.

Here we are using Zenrows, which is used to collect content from any website with a simple call. ZenRows handles rotating proxies, headless browsers and CAPTCHAs for you. ZenRows will bypass any anti-bot or blocking system to help you obtain the info you are looking for.


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
