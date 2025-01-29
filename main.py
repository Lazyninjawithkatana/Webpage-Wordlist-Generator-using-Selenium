from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import os

# List of target URLs (Replace https://www.example.com)
urls = [
    "https://www.example.com",
    "https://www.example.com",
    "https://www.example.com"
]

#For chrome you need to download chromedriver
#browser = webdriver.Chrome()
#path = path/to/chromedriver
browser = webdriver.Firefox()

def extract_words(url):

    browser.get(url)

    # Extract all text from the page
    page_text = browser.find_element(By.TAG_NAME, "body").text

    # Filter words (only alphanumeric words with at least 3 letters)
    words = set(re.findall(r'\b[a-zA-Z]{3,}\b', page_text))

    # Create a filename based on domain name
    domain = url.split("//")[-1].split("/")[0]
    filename = f"wordlist_{domain}.txt"

    # Save words to a file
    with open(filename, "w", encoding="utf-8") as f:
        for word in sorted(words):
            f.write(word + "\n")

    print(f"Saved wordlist: {filename}")

# Process each URL
for url in urls:
    extract_words(url)

# Close browser
browser.quit()
