import os
import sys
import site
from django.core.wsgi import get_wsgi_application

# Add python site packages,you can use virtualenv also
site.addsitedir("C:/Program Files/Python39/Lib/site-packages")

# Add the app's directory to the PYTHONPATH
sys.path.append('H:/djangogirls-blog-photo')
sys.path.append('H:/djangogirls-blog-photo/mysite')

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangogirls-blog-photo.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangogirls-blog-photo.settings")

# import django
# django.setup()

application = get_wsgi_application()