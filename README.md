# Webpage-Wordlist-Generator-using-Selenium
Overview
This Python script automates word extraction from webpages using Selenium WebDriver. It visits specified URLs, extracts unique words from the webpage content, and saves them as individual wordlist files.

Features
Extracts words from multiple webpages
Filters and saves unique words (minimum 3 letters)
Generates a separate wordlist file for each domain
Supports Firefox (default) and Chrome (with minor modification)

1. Install Selenium
pip install selenium

How It Works
The script opens a list of target URLs.
It extracts all visible text from the <body> tag.
Filters words that are at least 3 characters long and only contain letters.
Saves the extracted words into a file

Example Use Cases
Pentesting: Use extracted wordlists for Gobuster, dirb, or other brute-force tools. (gobuster dir -u https://example.com -w wordlist_example.com.txt -x html,php,js,txt -t 50 -o gobuster_results.txt)
SEO & Analysis: Extract keywords from competitor websites.
Data Collection: Gather words for NLP, AI, or automation tasks.
