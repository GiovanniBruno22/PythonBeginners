import requests # API for interacting with internet
from bs4 import BeautifulSoup # web scraper

def getUserInput(article_title):
    answer = input(f"Would you like to read {article_title}? (yes/no): ").lower()
    
    if answer == 'yes':
        return False
    elif answer == 'y':
        return False
    elif answer == 'no':
        return True 
    elif answer == 'n':
        return True
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        getUserInput(article_title)  # Recursive call to prompt again


def main():
    dontReadFlag = True

    while dontReadFlag:
        # Get random wikipedia article
        base_url = "https://en.wikipedia.org"
        random_article_url = base_url + "/wiki/Special:Random"
        response = requests.get(random_article_url)

        # Parse HTML 
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract Title
        article_title = soup.title.string

        # Ask for if User wants to Read
        dontReadFlag = getUserInput(article_title)

    # Extract First Paragraph
    print(soup.find('p').text)

if __name__ == '__main__':
    main()