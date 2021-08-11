#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
#sys.path.insert(0,'../env/lib/python3.7/site-packages')
#sys.path.insert(0, '/usr/local/lib/python3.8/site-packages') #Pillow "got lost"
# https://static.everythingability.opalstacked.com/notes/flickguy_269C470D.png

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'toolstoolstools.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
