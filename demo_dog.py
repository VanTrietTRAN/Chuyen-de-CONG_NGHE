import os
import django
from django.db.models import Value
from django.db.models.fields.json import KT

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from polls.models import Dog


def main() -> None:
    # 1. Storing and querying for None
    Dog.objects.get_or_create(name="Max", defaults={"data": None})  # SQL NULL
    Dog.objects.get_or_create(name="Archie", defaults={"data": Value(None, output_field=Dog._meta.get_field("data"))})  # JSON null

    print(list(Dog.objects.filter(data=None).values_list("name", flat=True)))
    print(list(Dog.objects.filter(data=Value(None, output_field=Dog._meta.get_field("data"))).values_list("name", flat=True)))
    print(list(Dog.objects.filter(data__isnull=True).values_list("name", flat=True)))
    print(list(Dog.objects.filter(data__isnull=False).values_list("name", flat=True)))

    # 2. Key, index, and path transforms
    Dog.objects.get_or_create(
        name="Rufus",
        defaults={
            "data": {
                "breed": "labrador",
                "owner": {
                    "name": "Bob",
                    "other_pets": [
                        {"name": "Fishy"},
                    ],
                },
            }
        },
    )
    Dog.objects.get_or_create(name="Meg", defaults={"data": {"breed": "collie", "owner": None}})

    print(list(Dog.objects.filter(data__breed="collie").values_list("name", flat=True)))

    # 3. KT() expressions
    Dog.objects.get_or_create(
        name="Shep",
        defaults={
            "data": {
                "owner": {"name": "Bob"},
                "breed": ["collie", "lhasa apso"],
            }
        },
    )

    qs = Dog.objects.annotate(
        first_breed=KT("data__breed__1"), owner_name=KT("data__owner__name")
    ).filter(first_breed__startswith="lhasa", owner_name="Bob")

    print(list(qs.values_list("name", flat=True)))


if __name__ == "__main__":
    main()
