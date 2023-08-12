import requests # API for interacting with internet
from bs4 import BeautifulSoup # web scraper

def switch(answer):
    # switch statement to determine if user wants to read the article
    if answer == "y":
        return False
    elif answer == "yes":
        return False
    elif answer == "n":
        return True
    elif answer == "no":
        return True

readFlag = True

while readFlag:
    # Get random wikipedia article
    base_url = "https://en.wikipedia.org"
    random_article_url = base_url + "/wiki/Special:Random"
    response = requests.get(random_article_url)

    # Parse HTML 
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract Title
    article_title = soup.title.string

    # Ask for if User wants to Read
    answer = input(f"Would you like to read {article_title}? (y/n): ")
    readFlag = switch(answer.lower())

# Extract First Paragraph
print(soup.find('p').text)