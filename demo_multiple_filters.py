import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from polls.models import Blog2, Entry


def seed() -> None:
    beatles, _ = Blog2.objects.get_or_create(name="Beatles Blog", defaults={"tagline": ""})
    pop, _ = Blog2.objects.get_or_create(name="Pop Music Blog", defaults={"tagline": ""})

    Entry.objects.get_or_create(
        blog=beatles,
        headline="New Lennon Biography",
        defaults={"body_text": "", "pub_date": date(2008, 6, 1)},
    )
    Entry.objects.get_or_create(
        blog=beatles,
        headline="New Lennon Biography in Paperback",
        defaults={"body_text": "", "pub_date": date(2009, 6, 1)},
    )
    Entry.objects.get_or_create(
        blog=pop,
        headline="Best Albums of 2008",
        defaults={"body_text": "", "pub_date": date(2008, 12, 15)},
    )
    Entry.objects.get_or_create(
        blog=pop,
        headline="Lennon Would Have Loved Hip Hop",
        defaults={"body_text": "", "pub_date": date(2020, 4, 1)},
    )


def main() -> None:
    seed()

    qs1 = Blog2.objects.filter(
        entry__headline__contains="Lennon",
        entry__pub_date__year=2008,
    )
    print("Case 1 (single filter):", list(qs1.values_list("name", flat=True)))

    qs2 = Blog2.objects.filter(
        entry__headline__contains="Lennon",
    ).filter(
        entry__pub_date__year=2008,
    )
    print("Case 2 (chained filters):", list(qs2.values_list("name", flat=True)))


if __name__ == "__main__":
    main()
