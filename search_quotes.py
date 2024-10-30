# search_quotes.py
from models import Author, Quote

def search_by_author(name):
    author = Author.objects(fullname=name).first()
    if author:
        quotes = Quote.objects(author=author)
        return [quote.quote for quote in quotes]
    return []

def search_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    return [quote.quote for quote in quotes]

def search_by_tags(tags):
    tags_list = tags.split(',')
    quotes = Quote.objects(tags__in=tags_list)
    return [quote.quote for quote in quotes]

def main():
    while True:
        command = input("Enter command (name, tag, tags, exit): ")
        if command.startswith("name:"):
            name = command.split("name:")[1].strip()
            results = search_by_author(name)
            print("\n".join(results) if results else "No quotes found for this author.")
        elif command.startswith("tag:"):
            tag = command.split("tag:")[1].strip()
            results = search_by_tag(tag)
            print("\n".join(results) if results else "No quotes found for this tag.")
        elif command.startswith("tags:"):
            tags = command.split("tags:")[1].strip()
            results = search_by_tags(tags)
            print("\n".join(results) if results else "No quotes found for these tags.")
        elif command == "exit":
            break
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()
