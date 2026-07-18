import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


# ! Show pseudo code & Flow chart

# 1. Target URL from your class slides
url = "https://en.wikipedia.org/wiki/Cambodia"

try:
    # 2. Send a GET request to download the raw HTML content
    response = requests.get(url)
    response.raise_for_status()  # Ensures the request was successful

    # 3. Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # 4. Find all structural hyperlink tags (<a>) and extract their href URLs
    urls = []
    for tag in soup.find_all('a'):
        href = tag.get('href')
        if href:  # Filters out empty links
            urls.append(href)

    # 5. Open/create 'text.txt', write each URL on a new line, and close it
    with open('text.txt', 'w', encoding='utf-8') as file:
        for link in urls:
            file.write(link + '\n')

    print(
        f"Success! Extracted {len(urls)} links and saved them to 'text.txt'.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the webpage: {e}")


def get_all_internal_links(base_url):
    # * get link
    print("Hello world")
    # * let it find tags inside of the wikipedia page (the ones we need)

    # * extract the raw HTML tags

    # * Split the words (formatting the raw HTML tags to words)

    # * put the extracted clean tags into a file (CSV, txt..etc)
