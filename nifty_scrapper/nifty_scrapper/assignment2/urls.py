
from django.conf.urls import url
from nifty_scrapper.assignment2 import views


urlpatterns = [
    url(r'^sharable/$', views.SharableCodeView, name='sharable'),
    url(r'^view/$', views.ViewShareableSnippet, name='view'),
]