from django.core.management.base import BaseCommand
from datetime import date
from polls.models import Blog2, Entry, Author, Poll, Dog


class Command(BaseCommand):
    help = "Seed sample data for polls app (blogs, entries, authors, polls, dogs)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Clear seeded data before seeding again",
        )

    def handle(self, *args, **options):
        if options["clear"]:
            self._clear()

        beatles, _ = Blog2.objects.get_or_create(
            name="Beatles Blog", defaults={"tagline": "All the latest Beatles news."}
        )
        pop, _ = Blog2.objects.get_or_create(name="Pop Music Blog", defaults={"tagline": ""})

        entry1, _ = Entry.objects.get_or_create(
            blog=beatles,
            headline="New Lennon Biography",
            defaults={"body_text": "", "pub_date": date(2008, 6, 1)},
        )
        entry2, _ = Entry.objects.get_or_create(
            blog=beatles,
            headline="New Lennon Biography in Paperback",
            defaults={"body_text": "", "pub_date": date(2009, 6, 1)},
        )
        entry3, _ = Entry.objects.get_or_create(
            blog=pop,
            headline="Best Albums of 2008",
            defaults={"body_text": "", "pub_date": date(2008, 12, 15)},
        )

        joe, _ = Author.objects.get_or_create(name="Joe", defaults={"email": "joe@example.com"})
        john, _ = Author.objects.get_or_create(name="John", defaults={"email": "john@example.com"})
        paul, _ = Author.objects.get_or_create(name="Paul", defaults={"email": "paul@example.com"})
        entry3.authors.add(joe, john, paul)

        Poll.objects.get_or_create(question="Who is your favorite Beatle?", pub_date=date(2005, 5, 2))
        Poll.objects.get_or_create(question="What is your favorite album?", pub_date=date(2005, 5, 6))

        Dog.objects.get_or_create(name="Max", defaults={"data": None})
        Dog.objects.get_or_create(name="Archie", defaults={"data": None})

        self.stdout.write(self.style.SUCCESS("Seed completed."))

    def _clear(self):
        Blog2.objects.filter(name__in=["Beatles Blog", "Pop Music Blog"]).delete()
        Entry.objects.filter(headline__in=[
            "New Lennon Biography",
            "New Lennon Biography in Paperback",
            "Best Albums of 2008",
        ]).delete()
        Author.objects.filter(name__in=["Joe", "John", "Paul"]).delete()
        Poll.objects.filter(question__in=[
            "Who is your favorite Beatle?",
            "What is your favorite album?",
        ]).delete()
        Dog.objects.filter(name__in=["Max", "Archie"]).delete()
        self.stdout.write(self.style.WARNING("Cleared previous seed data."))