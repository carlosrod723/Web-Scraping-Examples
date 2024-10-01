# Import necessary libraries and packages
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Initialize the WebDriver
driver= webdriver.Chrome()

# Open the URL
url= 'https://www.homes.com/massachusetts/houses-for-sale/'
driver.get(url)

# Give the page time to load
time.sleep(5)

# Scroll down the page to load more properties (if applicable)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
time.sleep(3)

# Find all property containers
property_containers= driver.find_elements(By.CLASS_NAME, 'placard-container')

# Open the CSV file for writing
with open('massachusetts_properties.csv', 'w', newline= '') as file:
    writer= csv.writer(file)
    writer.writerow(['Property Title', 'Price', 'Details', 'Link'])  # Headers

    for container in property_containers:
        try:

            # Extract Property Title (Name)
            title= container.find_element(By.XPATH, ".//p[@class='property-name]").text
            
            # Extract Property Price
            price= container.find_element(By.XPATH, ".//p[@class='price-container']").text
            
            # Extract Property Details (Beds, Baths, etc.)
            details= container.find_element(By.XPATH, ".//ul[@class='detailed-info-container']").text
            
            # Extract Property Link
            link= container.find_element(By.XPATH, ".//a[contains(@href, '/property')]").get_attribute('href')
            
            # Write data to CSV
            writer.writerow([title, price, details, link])
        
        except Exception as e:

            # If there's an issue finding any of the details, continue to the next
            print(f'Error: {e}')
            continue

# Close the driver
driver.quit()
