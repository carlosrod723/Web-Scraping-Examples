# Import necessary libaries and packages
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Send a request to the website
url= 'http://books.toscrape.com'
response= requests.get(url)

# Parse the HTML content using BeautifulSoup
soup= BeautifulSoup(response.content, 'html.parser')

# Find the boook listings (titles, prices and availability)
books= soup.find_all('article', class_= 'product_pod')

book_titles= []
book_prices= []
book_availability= []

for book in books:

    # Extract the title
    title= book.h3.a['title']
    book_titles.append(title)

    # Extract book price
    price= book.find('p', class_= 'price_color').text
    book_prices.append(price)

    # Extract availability status
    availability= book.find('p', class_= 'instock availability').text.strip()
    book_availability.append(availability)

# Store the data in a DataFrame
df= pd.DataFrame({'Title': book_titles, 'Price': book_prices, 'Availability': book_availability})

# Save the data to a CSV file (sample)
df.sample(5).to_csv('sample_books.csv', index= False)

print('Scraping complete. Sample data saved to sample_books.csv')