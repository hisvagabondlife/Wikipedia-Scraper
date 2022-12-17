#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import random
from markdownify import MarkdownConverter

def md(soup, **options):
	return MarkdownConverter(**options).convert_soup(soup)

response = requests.get(
	url="https://en.wikipedia.org/wiki/Varanasi",
)
soup = BeautifulSoup(response.content, 'html.parser')


title = soup.find(id="firstHeading")
body = soup.find(id="bodyContent")
body = md(body)

#-------Write to file ----------
f = open("scraped_data.md", "a")
f.write(body)
f.close()

#------- Random link to follow-------
# Get all the links
allLinks = soup.find(id="bodyContent").find_all("a")
random.shuffle(allLinks)
linkToScrape = 0

for link in allLinks:
	# We are only interested in other wiki articles
	if link['href'].find("/wiki/") == -1: 
		continue
	
	# Use this link to scrape
	linkToScrape = link
	break

#print(linkToScrape)

