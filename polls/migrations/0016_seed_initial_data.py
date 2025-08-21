from django.db import migrations
from datetime import date


def forwards_func(apps, schema_editor):
    Blog2 = apps.get_model('polls', 'Blog2')
    Entry = apps.get_model('polls', 'Entry')
    Author = apps.get_model('polls', 'Author')
    Poll = apps.get_model('polls', 'Poll')
    Dog = apps.get_model('polls', 'Dog')

    beatles, _ = Blog2.objects.get_or_create(name='Beatles Blog', defaults={'tagline': 'All the latest Beatles news.'})
    pop, _ = Blog2.objects.get_or_create(name='Pop Music Blog', defaults={'tagline': ''})

    entry1, _ = Entry.objects.get_or_create(blog=beatles, headline='New Lennon Biography', defaults={'body_text': '', 'pub_date': date(2008, 6, 1)})
    entry2, _ = Entry.objects.get_or_create(blog=beatles, headline='New Lennon Biography in Paperback', defaults={'body_text': '', 'pub_date': date(2009, 6, 1)})
    entry3, _ = Entry.objects.get_or_create(blog=pop, headline='Best Albums of 2008', defaults={'body_text': '', 'pub_date': date(2008, 12, 15)})

    joe, _ = Author.objects.get_or_create(name='Joe', defaults={'email': 'joe@example.com'})
    john, _ = Author.objects.get_or_create(name='John', defaults={'email': 'john@example.com'})
    paul, _ = Author.objects.get_or_create(name='Paul', defaults={'email': 'paul@example.com'})
    entry3.authors.add(joe, john, paul)

    Poll.objects.get_or_create(question='Who is your favorite Beatle?', pub_date=date(2005, 5, 2))
    Poll.objects.get_or_create(question='What is your favorite album?', pub_date=date(2005, 5, 6))

    Dog.objects.get_or_create(name='Max', defaults={'data': None})
    Dog.objects.get_or_create(name='Archie', defaults={'data': None})


def reverse_func(apps, schema_editor):
    Blog2 = apps.get_model('polls', 'Blog2')
    Entry = apps.get_model('polls', 'Entry')
    Author = apps.get_model('polls', 'Author')
    Poll = apps.get_model('polls', 'Poll')
    Dog = apps.get_model('polls', 'Dog')

    Entry.objects.filter(headline__in=[
        'New Lennon Biography',
        'New Lennon Biography in Paperback',
        'Best Albums of 2008',
    ]).delete()

    Author.objects.filter(name__in=['Joe', 'John', 'Paul']).delete()
    Poll.objects.filter(question__in=['Who is your favorite Beatle?', 'What is your favorite album?']).delete()
    Blog2.objects.filter(name__in=['Beatles Blog', 'Pop Music Blog']).delete()
    Dog.objects.filter(name__in=['Max', 'Archie']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_entrydetail'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]