"""LM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib.staticfiles import views
from django.contrib import admin
from django.conf import settings
#from rest_framework.schemas import get_schema_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('management.urls')),
    url(r'^api/', include('testrestapi.urls')),
    url(r'^api/', include('management.api')),
    
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', views.static.serve, {'document_root': settings.STATIC_ROOT}, name="static"),
        url(r'^media/(?P<path>.*)$', views.static.serve, {'document_root': settings.MEDIA_ROOT}, name="media")
    ]
