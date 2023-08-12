import wikipedia

def main():
    wikipedia.set_lang("en")  # Set the language to English

    while True:
        random_article = wikipedia.random()
        print("Random Article Title:", random_article)

        user_choice = input("Do you want to read this article? (yes/no): ").lower()
        if user_choice == "yes":
            try:
                article_content = wikipedia.page(random_article).content
                print("\nFull Article Content:\n")
                print(article_content)
                break
            except wikipedia.exceptions.DisambiguationError as e:
                print("This is a disambiguation page. Fetching another article...\n")
            except wikipedia.exceptions.PageError as e:
                print("Page not found. Fetching another article...\n")
        elif user_choice == "no":
            print("\nFetching another random article...\n")
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
  main()
