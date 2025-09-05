import requests
from bs4 import BeautifulSoup
import json
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# Send a GET request to the website

from selenium.webdriver.common.by import By
from urllib.parse import urljoin

service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")  # Run in headless mode
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://shamela.ws/book/11788/2')
driver.implicitly_wait(10)  # Wait for dynamic content
html = driver.page_source

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all the program divs
program_divs = soup.find_all("div", class_="nass")

for i, div in enumerate(program_divs, 1):

    # Get text content and clean it
    text = div.get_text(
        # separator=" "        ,
         strip=True)
    
    # Remove extra spaces and line breaks
    cleaned_text = ' '.join(text.split())
    
    print(f"\n--- Text Block {i} ---\n")
    print(cleaned_text)
    print("\n" + "-"*50 + "\n")


driver.quit()