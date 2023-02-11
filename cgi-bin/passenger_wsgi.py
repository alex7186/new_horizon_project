"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os, sys


sys.path.insert(0, "/var/www/u1734296/data/djangoenv/lib/python3.8/site-packages")
sys.path.insert(
    1,
    "/var/www/u1734296/data/www/xn-----dlccmbc8bcwbhe5aeehd9dxgi.xn--p1ai/new_horizon",
)


# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "main.settings"


from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
