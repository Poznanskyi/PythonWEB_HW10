import os
import django

from pymongo import MongoClient

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw_project.settings')
django.setup()

from quotes.models import Quote, Tag, Author  # noqa

client = MongoClient("mongodb+srv://poz:bN342Po12@firstcluster.dxzj24g.mongodb.net/test")

db = client.hw_django

authors = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
        name=author['name'],
        born_date=author['born'],
        born_location=author['location'],
        description=author['bio']
    )

quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    exist_quote = bool(len(Quote.objects.filter(quote=quote['quote'])))

    if not exist_quote:
        author = db.authors.find_one({'_id': quote['author']})
        a = Author.objects.get(name=author['name'])
        q = Quote.objects.create(
            quote=quote['quote'],
            author=a
        )
        for tag in tags:
            q.tag.add(tag)