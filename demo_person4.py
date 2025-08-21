import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from polls.models import Person4, MyPerson


def main() -> None:
    # Create base model instance (proxy = MyPerson over Person4)
    Person4.objects.get_or_create(first_name="foobar", last_name="demo")

    # Retrieve via proxy
    obj = MyPerson.objects.get(first_name="foobar")

    print(obj.first_name)  # foobar
    print(type(obj).__name__)  # MyPerson
    print(obj)  # __str__ of base/proxy (may show object id if not defined)


if __name__ == "__main__":
    main()

