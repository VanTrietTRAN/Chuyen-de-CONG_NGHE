import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from polls.models import Person


def main() -> None:
    person, created = Person.objects.get_or_create(
        first_name="Fred",
        last_name="Flintstone",
        defaults={"shirt_size": "L"},
    )

    if not created:
        person.shirt_size = "L"
        person.save()

    print(person.shirt_size)
    print(person.get_shirt_size_display())


if __name__ == "__main__":
    main() 