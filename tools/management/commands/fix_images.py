from django.core.management.base import BaseCommand, CommandError
from tools.models import *
import glob, os
import csv
import requests
import shutil
import PIL
from PIL import Image

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
    return dst

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

            tools = Activity.objects.all()
            for tool in tools:
                #tool = Tool.objects.first()
                try:
                    if tool.image:
                        url = tool.image

                        fname = url.split("/")[-1] # get the last item

                        #fix up bloody emojis and the like
                        dst = fix_filename(fname)

                        imagepath =  '/static/icons/' + dst
                        print(imagepath)
                        tool.image = imagepath
                        tool.save()

                        #os.remove(fullpath) #get rid of the big one.
                except Exception as err:
                    print(tool.name)
                    print(err)

   

        except Exception as err:
            raise CommandError( str(err))


        self.stdout.write(self.style.SUCCESS('Done!'))