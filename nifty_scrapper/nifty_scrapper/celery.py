from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab
from nifty_scrapper.scrapper.tasks import scrapper
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nifty_scrapper.settings')

from django.conf import settings  # noqa

app = Celery('nifty_scrapper')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# @app.task()
# def scrapper():
# 	print("HEllo celery!")

# @app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute=15, hour=0, day_of_week='mon,tue,wed,thu,fri,sat,sun'),
        scrapper.s()
    )

    # when i try this it work of every 1 min
    sender.add_periodic_task(
         crontab(minute='*/1'),
         scrapper.s()
   )
