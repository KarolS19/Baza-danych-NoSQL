# import_data.py
import json
from models import Author, Quote

def load_authors(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for item in data:
        author = Author(
            fullname=item['fullname'],
            born_date=item['born_date'],
            born_location=item['born_location'],
            description=item['description']
        )
        author.save()
    print("Authors imported successfully.")

def load_quotes(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for item in data:
        author = Author.objects(fullname=item['author']).first()
        if author:
            quote = Quote(
                tags=item['tags'],
                author=author,
                quote=item['quote']
            )
            quote.save()
    print("Quotes imported successfully.")

# Wywołanie funkcji
load_authors("authors.json")
load_quotes("quotes.json")
