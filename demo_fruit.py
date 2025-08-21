import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from polls.models import Fruit


def main() -> None:
    fruit = Fruit.objects.create(name="Apple")
    fruit.name = "Pear"
    fruit.save()

    names = list(Fruit.objects.values_list("name", flat=True))
    print(names)


if __name__ == "__main__":
    main() 