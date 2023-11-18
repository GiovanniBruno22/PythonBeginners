
import webbrowser # to open URLs in a web browser

import requests # to make HTTP requests and scrape the web
from bs4 import BeautifulSoup # HTML parser

def get_user_input(article_title):
    answer = input(f"Would you like to read {article_title}? (yes/no): ").lower()
    
    if answer.startswith('y'):
        return True
    elif answer.startswith('n'):
        return False
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        get_user_input(article_title)  # Recursive call to prompt again


def main():
    read = False
    url = None

    while not read:
        # Get random wikipedia article
        random_article_url = "https://en.wikipedia.org/wiki/Special:Random"
        response = requests.get(random_article_url)
        url = response.url

        # Parse HTML 
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract Title
        article_title = soup.title.string

        # Ask for if User wants to Read
        read = get_user_input(article_title)

    # Extract First Paragraph
    print("Opening in web browser...")
    webbrowser.open(url)

if __name__ == '__main__':
    main()