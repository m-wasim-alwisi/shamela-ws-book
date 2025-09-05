<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Scraping Script Documentation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
            background-color: #f8f9fa;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        h2 {
            color: #2980b9;
            margin-top: 25px;
        }
        h3 {
            color: #3498db;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: monospace;
        }
        pre {
            background-color: #f8f8f8;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            border-left: 4px solid #3498db;
        }
        ul, ol {
            margin-left: 20px;
        }
        li {
            margin-bottom: 8px;
        }
        .note {
            background-color: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 15px;
            margin: 20px 0;
            border-radius: 4px;
        }
        .disclaimer {
            background-color: #f8d7da;
            border-left: 4px solid #dc3545;
            padding: 15px;
            margin: 20px 0;
            border-radius: 4px;
        }
        a {
            color: #007bff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Web Scraping Script with Selenium and BeautifulSoup</h1>
        <p>This script demonstrates how to scrape content from a website using Selenium WebDriver and BeautifulSoup in Python.</p>

        <h2>Features</h2>
        <ul>
            <li>Automatically installs ChromeDriver using <code>chromedriver_autoinstaller</code></li>
            <li>Uses headless Chrome browser for efficient scraping</li>
            <li>Extracts and cleans text content from specific HTML elements</li>
            <li>Handles dynamic content with implicit waits</li>
        </ul>

        <h2>Requirements</h2>
        <ul>
            <li>Python 3.x</li>
            <li>Chrome browser installed on your system</li>
        </ul>
        
        <h3>Required Python packages:</h3>
        <ol>
            <li><code>requests</code></li>
            <li><code>beautifulsoup4</code></li>
            <li><code>selenium</code></li>
            <li><code>chromedriver_autoinstaller</code></li>
        </ol>

        <h2>Installation</h2>
        <p>Install the required packages:</p>
        <pre><code>pip install requests beautifulsoup4 selenium chromedriver_autoinstaller</code></pre>
        <p>Ensure you have Chrome browser installed on your system</p>

        <h2>Usage</h2>
        <p>The script currently targets <a href="https://shamela.ws/book/11788/2" target="_blank">https://shamela.ws/book/11788/2</a> and extracts text from all elements with class "nass". You can modify the URL and CSS selector as needed for your specific use case.</p>

        <h2>Code Example</h2>
        <pre><code>import requests
from bs4 import BeautifulSoup
import json
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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
    text = div.get_text(strip=True)
    
    # Remove extra spaces and line breaks
    cleaned_text = ' '.join(text.split())
    
    print(f"\n--- Text Block {i} ---\n")
    print(cleaned_text)
    print("\n" + "-"*50 + "\n")

driver.quit()</code></pre>

        <h2>Code Overview</h2>
        <ul>
            <li>Sets up Chrome WebDriver in headless mode</li>
            <li>Navigates to the target webpage</li>
            <li>Waits for dynamic content to load</li>
            <li>Parses HTML with BeautifulSoup</li>
            <li>Extracts and cleans text content from specified elements</li>
            <li>Prints formatted output with separators</li>
        </ul>

        <div class="note">
            <h2>Important Notes</h2>
            <ul>
                <li>Web scraping may violate terms of service for some websites</li>
                <li>Always check a website's <code>robots.txt</code> file before scraping</li>
                <li>Be respectful of server resources and implement delays if needed</li>
                <li>The website structure may change, requiring updates to the selectors</li>
            </ul>
        </div>

        <div class="disclaimer">
            <h2>Disclaimer</h2>
            <p>This script is for educational purposes only. Ensure you have permission to scrape data from any website you target.</p>
        </div>

        <h2>Useful Links</h2>
        <ul>
            <li><a href="https://www.selenium.dev/documentation/" target="_blank">Selenium Documentation</a></li>
            <li><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="_blank">BeautifulSoup Documentation</a></li>
            <li><a href="https://requests.readthedocs.io/en/latest/" target="_blank">Requests Library</a></li>
            <li><a href="https://pypi.org/project/chromedriver-autoinstaller/" target="_blank">ChromeDriver Autoinstaller</a></li>
        </ul>
    </div>
</body>
</html>
