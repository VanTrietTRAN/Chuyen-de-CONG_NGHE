import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from polls.models import Place, Restaurant


def main() -> None:
    # Ensure a Restaurant (and its parent Place) exist
    rest, _ = Restaurant.objects.get_or_create(
        name="Bob's Cafe",
        defaults={"serves_hot_dogs": True, "serves_pizza": False},
    )

    # Equivalent to the shell filters
    print(list(Place.objects.filter(name="Bob's Cafe").values_list("name", flat=True)))
    print(list(Restaurant.objects.filter(name="Bob's Cafe").values_list("name", flat=True)))

    # Access child from parent via multi-table inheritance
    p = Place.objects.get(pk=rest.pk)
    print(p.restaurant)  # Restaurant instance (uses __str__)


if __name__ == "__main__":
    main() 