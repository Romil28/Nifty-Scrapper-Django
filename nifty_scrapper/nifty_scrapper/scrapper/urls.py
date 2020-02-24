
from django.conf.urls import url
# from nifty_scrapper.scrapper.views import NiftyView
from nifty_scrapper.scrapper import views
urlpatterns = [
    url(r'^nifty/$', views.index, name='nifty'),
]