from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from django.conf import settings

from django.conf.urls.defaults import *

urlpatterns = [
    url(r'^$', views.index, name='index'),

]
