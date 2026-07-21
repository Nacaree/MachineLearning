import requests
from bs4 import BeautifulSoup
# ! Show pseudo code & Flow chart

url = "https://en.wikipedia.org/wiki/Cambodia"

headers = {
    "User-Agent": "CambodiaLinkScraper/1.0 (wikipedia:en; User:SothVi)"
}

try:
    # 1. Download the webpage
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Ensures the request was successful

    # 2. Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # 3. Find the main container that stores the 3 paragraphs
    content = soup.find(id='mw-content-text')

    # 4. Find article paragraphs and extract their text
    if content:
        paragraphs = []
        for paragraph in content.select('section > p'):
            # ? 'section > p' means it only takes <p> tags thats directly inside of the <section> tag.
            #! if <p> for example is inside of another tag such as <div> it will not take that <p> tag.
            text = paragraph.get_text(' ', strip=True)
            # only appends if the text is not empty, literally (if text != "")
            if text != "":
                paragraphs.append(text)

    # 5. Write the first three paragraphs to text.txt
        with open('text.txt', 'w', encoding='utf-8') as file:
            # ? paragraphs[:3] selects the first 3 paragraphs
            for text in paragraphs[:3]:
                file.write(text + '\n\n')

    # * show success message
        print(f"extracted the first 3 paragraphs and saved them to 'text.txt'.")
    else:
        print("Could not find the article content.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the webpage: {e}")
