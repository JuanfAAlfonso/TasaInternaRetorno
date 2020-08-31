from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^getServerState/(?P<fecha_peticion>[^/]*)/(?P<informacion_transaccion>[^/]*)/$', views.obtener_tir),
]