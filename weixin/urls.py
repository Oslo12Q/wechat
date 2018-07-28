from django.conf.urls import  include, url
from . import views

from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    url(r'^$',weixin),
    url(r'^create/$',createMenu),
]