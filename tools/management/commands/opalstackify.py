from django.core.management.base import BaseCommand, CommandError
from tools.models import *
import glob, os
import csv
import requests
import shutil
import PIL
from PIL import Image
'''
def fix_filename(fname):
    dst = fname.replace("🔊", "")
    dst = dst.replace("—", "")
    dst = dst.replace("_-_", "_")
    dst = dst.replace("_–_", "_")
    dst = dst.replace("__", "_")
    dst = dst.replace("__", "_")
    dst = dst.replace(" ", "")
    dst = dst.replace("®", "")
    dst = dst.replace("'", "")
    dst = dst.replace(" ", "")
    dst = dst.replace("👾", "")
    dst = dst.replace("🎵", "")
    dst = dst.replace(".jpg", ".png")
    dst = dst.replace("_small", "")
    return dst'''
def alter_image(item):
    try:
        if item.image:
            url = item.image
            if "http://tomsmith.webfactional.com/" in url:
                url = url.replace("http://tomsmith.webfactional.com/", "https://static.everythingability.opalstacked.com/")
                print( url )
                item.image = url
                item.save()

    except Exception as err:
        print(item.name)
        print(err)

def alter(item):
    try:
        if item.image_url:
            url = item.image_url
            if "http://tomsmith.webfactional.com/" in url:
                url = url.replace("http://tomsmith.webfactional.com/", "https://static.everythingability.opalstacked.com/")
                print( url )
                item.image_url = url
                item.save()

    except Exception as err:
        print(item.name)
        print(err)

dir_path = os.path.dirname(os.path.realpath(__file__))
class Command(BaseCommand):
    # python manage.py import_tools file="tools.csv"
    help = ''

    def add_arguments(self, parser):
        ''#parser.add_argument('file',  type=str)

    ########## MADE A REAL ISSUE WITH THIS ###################


    def handle(self, *args, **options):
        #filename  = options['file']
        try:
            #### start ######
            tools = Tool.objects.all()
            for item in tools:alter(item)

            activities = Activity.objects.all()
            for item in activities:alter_image(item)

            resources = Resource.objects.all()
            for item in resources:alter(item)

            inspirations = Inspiration.objects.all()
            for item in inspirations: alter(item)

            pages = Page.objects.all()
            for item in pages: alter(item)

            learnings = Learning.objects.all()
            for item in learnings: alter( item )

                
            ####### end #####
   
        except Exception as err:
            raise CommandError( str(err))


        self.stdout.write(self.style.SUCCESS('Done!'))