import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from polls.models import Blog2, Entry, Author


def main() -> None:
    # Create and save a Blog
    b = Blog2(name="Beatles Blog", tagline="All the latest Beatles news.")
    b.save()

    # Update a Blog instance (simulate b5 from shell; here use the same b)
    b.name = "New name"
    b.save()

    # Prepare an Entry and a target Blog
    entry, _ = Entry.objects.get_or_create(pk=1, defaults={
        "blog": b,
        "headline": "Initial headline",
        "body_text": "",
    })

    cheese_blog, _ = Blog2.objects.get_or_create(name="Cheddar Talk")
    entry.blog = cheese_blog
    entry.save()

    # Create an Author and add to Entry
    joe, _ = Author.objects.get_or_create(name="Joe")
    entry.authors.add(joe)

    # Create multiple Authors and add at once
    john, _ = Author.objects.get_or_create(name="John")
    paul, _ = Author.objects.get_or_create(name="Paul")
    george, _ = Author.objects.get_or_create(name="George")
    ringo, _ = Author.objects.get_or_create(name="Ringo")
    entry.authors.add(john, paul, george, ringo)

    # Print some results for visibility
    print("Blog names:", list(Blog2.objects.values_list("name", flat=True)))
    print("Entry blog:", entry.blog.name)
    print("Entry authors:", list(entry.authors.values_list("name", flat=True)))


if __name__ == "__main__":
    main()
