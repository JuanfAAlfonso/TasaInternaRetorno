import datetime
import json
from .models import Dividendos

from django.http import HttpResponse


def obtener_tir(request, text):
    if request.method == "GET":
        #json_informacion = json.loads(informacion_transaccion)
        #for transaccion in json_informacion:
            #print(transaccion)
        # fecha = datetime.datetime.strptime(transaccion['fecha'], "%Y-%m-%dT%H:%M:%S%z")
        # acciones = transaccion['acciones']
        # valor = transaccion['valor']
        return HttpResponse(text, content_type='application/json')


def calcular_dividendos():
    pass
