from django.conf.urls import  include, url
from django.conf import settings
from django.conf.urls.static import static


from .views import *

urlpatterns = [
    url(r'^$',oslo),
    url(r'^search_name/$',search_name),
    url(r'^oslo/$',destical),
    url(r'^err/$',err_destical),
    url(r'^qr_code/$',qr_code),
    url(r'^oc_img/$',oc_img),
]
