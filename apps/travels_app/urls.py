from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^create', views.create, name='create'),
    url(r'^process', views.process, name='process'),
    url(r'^destination/(?P<locale_id>\d+)$', views.destination, name='destination'),
    url(r'^join/(?P<trip_id>\d+)$', views.join, name='join'),
]