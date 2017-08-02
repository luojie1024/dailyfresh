from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.order),
    url(r'^addorder/$', views.order_handle),
    url(r'^pay&(\d+)/$', views.pay),
]
