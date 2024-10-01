# Import necessary libraries and packages
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Base URL of the job board
base_url= 'https://remoteok.com'

# Create lists to store job data
job_titles= []
company_names= []
locations= []
links= []

# Loop through the first 3 pages of job listings (adding pagination)
for page in range(1,4):
    url= base_url.format(page)
    headers= {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    response= requests.get(url, headers= headers)

    # Check if the page request was successful
    if response.status_code != 200:
        print(f'Failed to retrieve page {page}')
        continue

    # Parse the HTML content
    soup= BeautifulSoup(response.content, 'html.parser')

    # Find all the job listings
    jobs= soup.find_all('tr', class_= 'job')

    for job in jobs:

        # Extract job title and clean up whitespace
        title= job.find('h2', {'itemprop': 'title'})
        job_titles.append(title.text.strip() if title else 'N/A')

        # Extract company name and clean up whitespace
        company= job.find('h3', {'itemprop': 'name'})
        company_names.append(company.text.strip() if company else 'N/A')

        # Extract job location and clean up whitespace
        location= job.find('div', class_='location')
        locations.append(location.text.strip() if location else 'Remote')

        # Extract the link to the job posting
        link= job.find('a', class_='preventLink')
        links.append(f"https://remoteok.com{link['href']}" if link else 'N/A')

# Create a DataFrame with the collected data
df= pd.DataFrame({'Job Title': job_titles, 'Company': company_names, 'Location': locations, 'Job Link': links})

# Save the data to a CSV (sample)
df.to_csv('sample_job_postings.csv', index= False)

print('Scraping complete. Data saved to sample_job_postings.csv')