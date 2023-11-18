import wikipedia

def get_user_input(article_title):
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
        get_user_input(article_title)  # Recursive call to prompt again

def main():
    # Set the language for the Wikipedia instance (e.g., 'en' for English)
    wikipedia.set_lang("en") 

    # Set while loop flag
    do_not_read = True

    while do_not_read:
        # Get a random article title
        article_title = wikipedia.random()

        # Ask for if User wants to Read
        do_not_read = get_user_input(article_title)

    # Fetch the content of the random article
    article_content = wikipedia.page(article_title)
    print(article_content.summary)

if __name__ == '__main__':
    main()