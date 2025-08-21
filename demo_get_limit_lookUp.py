import os
import django
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from polls.models import Blog2, Entry


def ensure_seed() -> None:
    beatles_blog, _ = Blog2.objects.get_or_create(
        name="Beatles Blog",
        defaults={"tagline": "All the latest Beatles news."},
    )

    # Ensure pk=1 exists
    Entry.objects.get_or_create(
        pk=1,
        defaults={
            "blog": beatles_blog,
            "headline": "Cat bites dog",
            "body_text": "",
            "pub_date": datetime.date(2005, 1, 31),
        },
    )

    # More entries for slicing/order/lookups
    data = [
        ("What happened yesterday", datetime.date(2005, 2, 1)),
        ("What we learned", datetime.date(2006, 1, 2)),
        ("Lennon writes song", datetime.date(2004, 12, 31)),
        ("Another headline", datetime.date(2007, 5, 20)),
        ("Zebra crossing", datetime.date(2001, 6, 18)),
        ("Yellow Submarine", datetime.date(2003, 7, 7)),
        ("Hello Goodbye", datetime.date(2002, 8, 8)),
    ]

    for headline, pub_date in data:
        Entry.objects.get_or_create(
            blog=beatles_blog,
            headline=headline,
            defaults={
                "body_text": "",
                "pub_date": pub_date,
            },
        )


def main() -> None:
    ensure_seed()

    # 1. Retrieving a single object with get()
    one_entry = Entry.objects.get(pk=1)
    print("one_entry:", one_entry.headline)

    # 2. Limiting QuerySets (slicing)
    print("slice [:5]:", list(Entry.objects.all()[:5].values_list("headline", flat=True)))
    print("slice [5:10]:", list(Entry.objects.all()[5:10].values_list("headline", flat=True)))
    print("slice [:10:2]:", list(Entry.objects.all()[:10:2].values_list("headline", flat=True)))
    print("order_by first:", Entry.objects.order_by("headline")[0].headline)
    print("order_by [0:1].get():", Entry.objects.order_by("headline")[0:1].get().headline)

    # 3. Field lookups
    print(
        "pub_date__lte 2006-01-01:",
        list(Entry.objects.filter(pub_date__lte="2006-01-01").values_list("headline", flat=True)),
    )

    # a. exact
    print("exact Cat bites dog:", Entry.objects.get(headline__exact="Cat bites dog").pk)

    # b. iexact (use Blog2)
    print("Blog2 iexact beatles blog:", Blog2.objects.get(name__iexact="beatles blog").name)

    # c. contains
    print("contains Lennon:", Entry.objects.get(headline__contains="Lennon").headline)


if __name__ == "__main__":
    main()
