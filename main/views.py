import json

from django.shortcuts import render
from django.http import HttpResponse


def guardar_transacciones(request, informacion_transaccion):
    json_informacion = json.loads(informacion_transaccion)
    pass


def obtener_tir(request):
    if request.method == "GET":
        return HttpResponse(json.dumps({"status": "ACTIVO"}), content_type='application/json')


def calcular_dividendos():
    pass
