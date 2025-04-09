import wikipedia

MAXIMUM_SENTENCES = 5
MAXIMUM_RESULTS = 1

page_title = input("Enter page title: ").title()
while page_title != "":
    try:
        page = wikipedia.page(f"{page_title}")
        wikipedia.page(f"{page_title}")
        print("\n".join(wikipedia.search(f"{page_title}", results = MAXIMUM_RESULTS)))
        print(wikipedia.summary(f"{page_title}", sentences = MAXIMUM_SENTENCES))
        print(page.url)
    except wikipedia.exceptions.PageError:
        print(f"Page id \"{page_title}\" does not match any pages. Try another id!")
    except wikipedia.exceptions.DisambiguationError:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(wikipedia.search(f"{page_title}"))
    print()
    page_title = input("Enter page title: ").title()

print("Thank you.")
