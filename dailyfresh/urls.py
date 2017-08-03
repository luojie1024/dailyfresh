"""dailyfresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from df_goods import search_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('df_user.urls')),
    url(r'^cart/', include('df_cart.urls')),
    url(r'^goods/', include('df_goods.urls')),
    url(r'^order/', include('df_order.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include('df_goods.urls', namespace='goods')),
    url(r'^search/', search_views.MySeachView(), name='haystack_search'),
]
