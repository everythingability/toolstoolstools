from django.core.management.base import BaseCommand, CommandError
from tools.models import Tool,Category, Tag, Resource
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
            tools = Tool.objects.all()

            for tool in tools:
                print( tool.name, tool.category,tool.altcategory )

                tag, created = Tag.objects.get_or_create(name=tool.category.name)
                tool.tags.add(tag)
                tag, created = Tag.objects.get_or_create(name=tool.altcategory.name)
                tool.tags.add(tag)
                tool.save()
            
            resources = Resource.objects.all()

            for resource in resources:
                print( resource.name, resource.category,resource.altcategory )

                tag, created = Tag.objects.get_or_create(name=resource.category.name)
                resource.tags.add(tag)
                tag, created = Tag.objects.get_or_create(name=resource.altcategory.name)
                resource.tags.add(tag)
                resource.save()
   

        except Exception as err:
            raise CommandError( str(err))


        self.stdout.write(self.style.SUCCESS('Done!'))