import os
import django
from datetime import date
from django.db.models import Q

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from polls.models import Poll


def seed() -> None:
    Poll.objects.get_or_create(question="Who is your favorite Beatle?", pub_date=date(2005, 5, 2))
    Poll.objects.get_or_create(question="What is your favorite album?", pub_date=date(2005, 5, 6))
    Poll.objects.get_or_create(question="Who will win?", pub_date=date(2006, 1, 1))
    Poll.objects.get_or_create(question="What happened?", pub_date=date(2004, 12, 31))


def main() -> None:
    seed()

    # Single LIKE query
    q_like = Q(question__startswith="What")
    print("Q(question__startswith='What') ->", list(Poll.objects.filter(q_like).values_list("question", flat=True)))

    # OR query
    q_or = Q(question__startswith="Who") | Q(question__startswith="What")
    print("Who OR What ->", list(Poll.objects.filter(q_or).values_list("question", flat=True)))

    # OR + NOT
    q_complex = Q(question__startswith="Who") | ~Q(pub_date__year=2005)
    print("Who OR NOT pub_year=2005 ->", list(Poll.objects.filter(q_complex).values_list("question", flat=True)))

    # Mixed with get(), positional Q args are ANDed
    obj = Poll.objects.get(
        Q(question__startswith="Who"),
        Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)),
    )
    print("get with OR pub_date ->", obj.question)

    # Valid: Q first, then kwargs (also ANDed together)
    obj2 = Poll.objects.get(
        Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)),
        question__startswith="Who",
    )
    print("get with Q then kwargs ->", obj2.question)

    # Invalid example (do not run): kwargs before Q would raise TypeError
    print("Note: kwargs before Q would be invalid and raise an error.")


if __name__ == "__main__":
    main()
