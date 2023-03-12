"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

# import sys  # pridane kvoli apache

from django.core.wsgi import get_wsgi_application

# from pathlib import Path    # pridane kvoli apache

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Add project directory to the sys.path - pridane kvoli apache
# path_home = str(Path(__file__).parents[1])
# if path_home not in sys.path:
#   sys.path.append(path_home)  # az potialto

application = get_wsgi_application()

# sys.path.append('/mysite')
# sys.path.append('/djangogirls-blog-photo/mysite')
