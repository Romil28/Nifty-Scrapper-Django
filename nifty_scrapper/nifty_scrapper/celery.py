from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab
from nifty_scrapper.scrapper.tasks import scrapper
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nifty_scrapper.settings')

from django.conf import settings  # noqa

app = Celery('nifty_scrapper')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(
#          crontab(minute='*/15'),
#          scrapper.s()
#    )
