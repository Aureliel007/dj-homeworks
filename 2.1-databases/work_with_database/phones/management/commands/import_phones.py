import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            slug = slugify(phone['name'])
            Phone.objects.create(**phone, slug=slug)
