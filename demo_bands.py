import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from polls.models import Person, Group, Membership


def main() -> None:
    ringo, _ = Person.objects.get_or_create(name="Ringo Starr")
    paul, _ = Person.objects.get_or_create(name="Paul McCartney")
    beatles, _ = Group.objects.get_or_create(name="The Beatles")

    Membership.objects.get_or_create(
        person=ringo,
        group=beatles,
        defaults={
            "date_joined": date(1962, 8, 16),
            "invite_reason": "Needed a new drummer.",
        },
    )

    print(list(beatles.members.values_list("name", flat=True)))
    print(list(ringo.group_set.values_list("name", flat=True)))

    Membership.objects.get_or_create(
        person=paul,
        group=beatles,
        defaults={
            "date_joined": date(1960, 8, 1),
            "invite_reason": "Wanted to form a band.",
        },
    )

    print(list(beatles.members.values_list("name", flat=True)))


if __name__ == "__main__":
    main() 