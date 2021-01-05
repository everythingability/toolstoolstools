from django.core.management.base import BaseCommand, CommandError
from tools.models import Tool,Category, Tag, Resource, Inspiration
import os
import csv
f = open("everything.tsv", 'w')
def write_item(Type, item):
    f.write("Tool"+"\t")
    tag = ""
    try:
        ''
        f.write(item.tags.first().name + "\t")
    except:
        ''
    f.write(item.name + "\t")
    f.write(item.url + "\t")
    f.write(item.image_url + "\t" )
    f.write(item.about.replace("\n", "|") )
    f.write("\n")

dir_path = os.path.dirname(os.path.realpath(__file__))
class Command(BaseCommand):
    # python manage.py import_tools file="tools.csv"
    help = 'Export everything as simple .csv'

    def add_arguments(self, parser):
        ''#parser.add_argument('file',  type=str)

  

    def handle(self, *args, **options):
        #filename  = options['file']
        try:
            
            items = Tool.objects.all()

            for item in items:
                write_item("Tool", item)
                
            
            items = Resource.objects.all()

            for item in items:
                write_item("Resource", item)

            items = Inspiration.objects.all()

            for item in items:
                write_item("Inspiration", item)

            f.close()
   

        except Exception as err:
            raise CommandError( str(err))


        self.stdout.write(self.style.SUCCESS('Done!'))