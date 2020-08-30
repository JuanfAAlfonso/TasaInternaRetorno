from django.urls import path

from . import views

urlpatterns = [
    path("getServerState/", views.obtener_tir),
]