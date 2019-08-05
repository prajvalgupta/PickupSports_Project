from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^email$', views.emailForm),
    url(r'^venueFormPath$', views.venueForm),
    url(r'^insertVenuePath$', views.insertVenue),
]