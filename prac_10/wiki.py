import wikipedia

MAXIMUM_SENTENCES = 5
MAXIMUM_RESULTS = 1

page_title = input("Enter page title: ")
while page_title != "":
    try:
        page = wikipedia.page(page_title, auto_suggest=False)
        print("\n".join(wikipedia.search(page, results = MAXIMUM_RESULTS)))
        print(wikipedia.summary(page, sentences = MAXIMUM_SENTENCES))
        print(page.url)

    except wikipedia.exceptions.PageError:
        print(f"Page id \"{page_title}\" does not match any pages. Try another id!")
    except wikipedia.exceptions.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print("(BeautifulSoup warning)")
        print(e.options)

    print()
    page_title = input("Enter page title: ")

print("Thank you.")
