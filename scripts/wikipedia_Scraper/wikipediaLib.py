import wikipedia

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

# Set the language for the Wikipedia instance (e.g., 'en' for English)
wikipedia.set_lang("en") 

# Set while loop flag
readFlag = True

while readFlag:
    # Get a random article title
    article_title = wikipedia.random()

    # Ask for if User wants to Read
    answer = input(f"Would you like to read {article_title}? (y/n): ")
    readFlag = switch(answer.lower())

# Fetch the content of the random article
article_content = wikipedia.page(article_title)
print(article_content.summary)