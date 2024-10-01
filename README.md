# Web Scraping Examples

## Overview

This repository contains three examples of web scraping using Python and Selenium. Each example demonstrates different web scraping techniques and methodologies to gather data from various websites. The goal is to collect data from an e-commerce site, a job listings site, and a real estate listings site. These examples show how to navigate different website structures, handle pagination, and extract useful data for analysis.

## Example 1: E-commerce Scraper

The first example is a straightforward web scraper for an e-commerce website. The goal is to collect product information such as the product title, price, and availability. The scraper navigates through the product listings on the webpage and extracts the necessary details.

Key Points:
- Extracts product title, price, and availability.
- Handles static content using BeautifulSoup.
- Example of scraping product data for market research or price comparison purposes.

Refer to the `ecommerce_scraper.py` script for implementation details, and you can also refer to the `sample_books.csv` file to view the sample data scraped.

## Example 2: Job Listings Scraper (with Pagination)

The second example involves scraping job listings from a job board. In addition to extracting job titles, company names, job locations, and job links, the scraper also handles pagination to retrieve data from multiple pages of job listings. This scraper is useful for gathering job market data, tracking open positions, or analyzing job trends.

Key Points:
- Extracts job title, company name, location, and link to the job posting.
- Handles pagination to collect data from multiple pages.
- Can be used to monitor job trends and market demand.

Refer to the `job_scraper.py` script for implementation details, and you can also refer to the `sample_job_postings.csv` file to view the sample data scraped.

## Example 3: Real Estate Scraper

The final example demonstrates how to scrape real estate listings from a property website. The scraper collects property details such as the title, price, number of bedrooms, bathrooms, square footage, and the link to the property listing. It handles dynamic content loading and is designed to collect data for real estate market analysis.

Key Points:
- Extracts property title, price, property details (beds, baths, square footage), and link to the property listing.
- Handles dynamically loaded data using Selenium.
- Useful for analyzing real estate market trends, comparing property prices, or conducting neighborhood analysis.

Refer to the `real_estate_scraper.py` script for implementation details, and you can also refer to the `massachusetts_properties.csv` file to view the sample data scraped.
