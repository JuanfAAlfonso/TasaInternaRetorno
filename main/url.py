from django.urls import path
from django.conf.urls import url, include
from rest_framework import serializers, viewsets, routers

from . import views

urlpatterns = [
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^getServerState/(?P<text>[^/]*)/$', views.obtener_tir),
]