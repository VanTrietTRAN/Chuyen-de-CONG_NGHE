import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from polls.models import Blog2, Entry, Author


def seed():
    # Blogs
    beatles, _ = Blog2.objects.get_or_create(name="Beatles Blog", defaults={"tagline": ""})
    pop, _ = Blog2.objects.get_or_create(name="Pop Music Blog", defaults={"tagline": ""})

    # Entries
    e1, _ = Entry.objects.get_or_create(
        blog=beatles,
        headline="New Lennon Biography",
        defaults={"body_text": "", "pub_date": date(2008, 6, 1)},
    )
    e2, _ = Entry.objects.get_or_create(
        blog=beatles,
        headline="New Lennon Biography in Paperback",
        defaults={"body_text": "", "pub_date": date(2009, 6, 1)},
    )
    e3, _ = Entry.objects.get_or_create(
        blog=pop,
        headline="Best Albums of 2008",
        defaults={"body_text": "", "pub_date": date(2008, 12, 15)},
    )

    # Authors
    john, _ = Author.objects.get_or_create(name="John", defaults={"email": "john@example.com"})
    paul, _ = Author.objects.get_or_create(name="Paul", defaults={"email": "paul@example.com"})

    # Link authors to entries
    e3.authors.add(john, paul)

    return beatles, pop, e1, e2, e3, john, paul


def main():
    beatles, pop, e1, e2, e3, john, paul = seed()

    # 1. One-to-many relationships
    # a) Forward: set FK to None if nullable, otherwise show note
    entry = e2  # simulate: Entry with id=2
    if Entry._meta.get_field("blog").null:
        entry.blog = None
        entry.save()
        print("Set entry.blog = None and saved.")
    else:
        print("Entry.blog is not nullable; skipping setting to None.")

    # b) Backward: Blog2 -> Entry via entry_set
    b = beatles  # simulate: Blog with id=1
    print("b.entry_set.all():", list(b.entry_set.values_list("headline", flat=True)))
    print(
        "b.entry_set.filter(headline__contains='Lennon'):",
        list(b.entry_set.filter(headline__contains="Lennon").values_list("headline", flat=True)),
    )
    print("b.entry_set.count():", b.entry_set.count())

    # 2. Many-to-many relationships
    e = e3  # simulate: Entry with id=3
    print("e.authors.all():", list(e.authors.values_list("name", flat=True)))
    print("e.authors.count():", e.authors.count())
    print(
        "e.authors.filter(name__contains='John'):",
        list(e.authors.filter(name__contains="John").values_list("name", flat=True)),
    )

    a = john  # simulate: Author with id=5
    print("a.entry_set.all():", list(a.entry_set.values_list("headline", flat=True)))


if __name__ == "__main__":
    main()
