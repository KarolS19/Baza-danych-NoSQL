from mongoengine import Document, StringField, ReferenceField, ListField, connect

connect(db="twoja_baza", host="mongodb+srv://użytkownik:hasło@cluster.mongodb.net/twoja_baza?retryWrites=true&w=majority")

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, required=True)
    quote = StringField(required=True)
