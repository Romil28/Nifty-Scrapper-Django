
from django.conf.urls import url
from nifty_scrapper.scrapper import views

urlpatterns = [
    url(r'^nifty/$', views.NiftyView, name='nifty'),
]