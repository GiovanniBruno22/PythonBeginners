import wikipedia

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
    # Set the language for the Wikipedia instance (e.g., 'en' for English)
    wikipedia.set_lang("en") 

    # Set while loop flag
    dontReadFlag = True

    while dontReadFlag:
        # Get a random article title
        article_title = wikipedia.random()

        # Ask for if User wants to Read
        dontReadFlag = getUserInput(article_title)

    # Fetch the content of the random article
    article_content = wikipedia.page(article_title)
    print(article_content.summary)

if __name__ == '__main__':
    main()