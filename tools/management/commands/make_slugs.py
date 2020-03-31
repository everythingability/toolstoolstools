from django.core.management.base import BaseCommand, CommandError
from tools.models import Tool,Category, Tag
from django.utils.text import slugify
import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
class Command(BaseCommand):
    # python manage.py import_tools file="tools.csv"
    help = 'meant to help me get started, importing a lot of initial data etc'

    def add_arguments(self, parser):
        ''#parser.add_argument('file',  type=str)

    def handle(self, *args, **options):
        #filename  = options['file']
        try:
            tags = Tag.objects.all()

            for tag in tags:
                slug = slugify(tag.name)
                tag.slug = slug
                tag.save()
                print( slug )
   

        except Exception as err:
            raise CommandError( str(err))


        self.stdout.write(self.style.SUCCESS('Done!'))