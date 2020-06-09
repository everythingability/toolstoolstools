from django.core.management.base import BaseCommand, CommandError
from tools.models import Tool,Category, Resource, Learning
import glob, os
import csv
import requests
import shutil
import PIL
from PIL import Image

dir_path = os.path.dirname(os.path.realpath(__file__))
class Command(BaseCommand):
    # python manage.py import_tools file="tools.csv"
    help = ''

    def add_arguments(self, parser):
        ''#parser.add_argument('file',  type=str)

    def handle(self, *args, **options):
        #filename  = options['file']
        try:
            #self.stdout.write(dir_path)
            #self.stdout.write(filename)
            tools = Tool.objects.all()
            for tool in tools:
                #tool = Tool.objects.first()
                try:
                    if tool.image_url:
                        url = tool.image_url
                        if "http" in tool.image_url: #only do remote ones, not local relative
                            fname = url.split("/")[-1]
                            
                            fullpath = '/Users/tomsmith/toolstoolstools/toolstoolstools/tools/static/images/' +fname #hack
                            print(fullpath)
                            response = requests.get(url, stream=False)
                            with open( fullpath , 'wb') as out_file:
                                response.raw.decode_content = True
                                shutil.copyfileobj(response.raw, out_file)
                            del response

                            #RESIZE IMAGE
                            mywidth = 300
                            img = Image.open(fullpath)
                            wpercent = (mywidth/float(img.size[0]))
                            hsize = int((float(img.size[1])*float(wpercent)))
                            img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)

                            new_fname = "".join(fname.split(".")[:-1]) + "_small.jpg"
                            
                            # FIX UP A WHOLE HEAP OF CRAP
                            
                            new_fname = new_fname.replace("🔊", "") # fixed up this...
                            #PHOTOMOSH_and_Desktop_—_tomsmith_web503___webapps_static_notes_—_ssh_tomsmith_tomsmith_webfactional_com_—_117×48_2289A191_small.jpg
                            new_fname = new_fname.replace("—", "") # fixed up this...
                            #Lynksoft_—_Create_Explore_Share_239E6C1B_small.jpg
                            print (new_fname)
                            new_fullpath = '/Users/tomsmith/toolstoolstools/toolstoolstools/tools/static/images/' + new_fname
                            img.save(new_fullpath)

                            tool.image_url = '/static/images/' + new_fname
                            tool.save()

                            os.remove(fullpath) #get rid of the big one.
                except Exception as err:
                    print(tool.name)
                    print(err)

   

        except Exception as err:
            raise CommandError( str(err))


        self.stdout.write(self.style.SUCCESS('Done!'))