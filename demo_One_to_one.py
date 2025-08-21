import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from polls.models import Blog2, Entry, EntryDetail


def ensure_seed() -> None:
    blog, _ = Blog2.objects.get_or_create(name="Seed Blog", defaults={"tagline": "demo"})

    e1, _ = Entry.objects.get_or_create(
        blog=blog,
        headline="First seed entry",
        defaults={"body_text": "", "pub_date": date(2020, 1, 1)},
    )
    e2, _ = Entry.objects.get_or_create(
        blog=blog,
        headline="Second seed entry",
        defaults={"body_text": "", "pub_date": date(2020, 1, 2)},
    )

    EntryDetail.objects.get_or_create(entry=e1, defaults={"details": "Details for first"})
    EntryDetail.objects.get_or_create(entry=e2, defaults={"details": "Details for second"})


def main() -> None:
    ensure_seed()

    try:
        ed = EntryDetail.objects.get(pk=2)
    except EntryDetail.DoesNotExist:
        # Fallback: pick the second EntryDetail by pk if available
        ed = EntryDetail.objects.order_by("pk")[1]

    print(ed.entry)  # Related Entry object


if __name__ == "__main__":
    main()
