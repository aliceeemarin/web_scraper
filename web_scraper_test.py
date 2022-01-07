"""
Website Scraper
Alice Marin Python Project

"""

# Import Beautiful Soup module
from bs4 import BeautifulSoup
# Substitute website as needed
with open("index.html", "r") as f:
	doc = BeautifulSoup(f, "html.parser")

# Change tags for tags desired
tags = doc.find_all("p")[0]
# Here you can print whatever you want to look at
print(tags.find_all("b"))