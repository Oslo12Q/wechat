"""search_Engines URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dev/', include('web_service.urls')),
    url(r'^weixin/',include('weixin.urls')),
    #url(R'^qr_code',include('er_db.urls')),
    url(r'^MP_verify_PNyE15nlc1gky07l.txt',mp_verify, name='mp_verify'),
    url(r'^oslo/$',oslo,name = 'oslo'),
    url(r'^$',xln,name='xln'),
    url(r'^love/$',love,name = 'love'),
]
#urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
if settings.DEBUG is False:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT}),
        url(r'^images/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    ]
