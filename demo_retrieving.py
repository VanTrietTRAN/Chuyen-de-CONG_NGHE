import os
import django
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from polls.models import Blog2, Entry


def main() -> None:
    # 1. Retrieving objects (Manager is on the class, not the instance)
    print(Blog2.objects)  # Manager

    b = Blog2(name="Foo", tagline="Bar")
    try:
        _ = b.objects
    except AttributeError:
        print('AttributeError: "Manager isn\'t accessible via Blog instances."')

    # 2. Retrieving all objects
    all_entries = Entry.objects.all()
    print("All entries count:", all_entries.count())

    # 3a. Chaining filters
    q = Entry.objects.filter(headline__startswith="What").exclude(
        body_text__icontains="food"
    )

    if hasattr(Entry, "pub_date"):
        q = Entry.objects.filter(headline__startswith="What").exclude(
            pub_date__gte=datetime.date.today()
        ).filter(pub_date__gte=datetime.date(2005, 1, 30))
        print("Chained with pub_date present ->", q)
    else:
        print("Note: Entry.pub_date not present; demonstrating chaining without pub_date")
        print("Chained without pub_date ->", q)

    # 3b. Filtered QuerySets are unique (sharing base QuerySet)
    q1 = Entry.objects.filter(headline__startswith="What")
    if hasattr(Entry, "pub_date"):
        q2 = q1.exclude(pub_date__gte=datetime.date.today())
        q3 = q1.filter(pub_date__gte=datetime.date.today())
        print("q1:", q1)
        print("q2:", q2)
        print("q3:", q3)
    else:
        q2 = q1.exclude(body_text__icontains="food")
        q3 = q1.filter(body_text__icontains="food")
        print("q1:", q1)
        print("q2 (no pub_date):", q2)
        print("q3 (no pub_date):", q3)

    # 3c. QuerySets are lazy
    q_lazy = Entry.objects.filter(headline__startswith="What")
    if hasattr(Entry, "pub_date"):
        q_lazy = q_lazy.filter(pub_date__lte=datetime.date.today())
    q_lazy = q_lazy.exclude(body_text__icontains="food")
    print(q_lazy)


if __name__ == "__main__":
    main()
