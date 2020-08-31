import datetime
import json

from django.http import HttpResponse
from django.db import connection
import pandas as pd
import numpy as np
import numpy_financial as npf


def obtener_tir(request, fecha_peticion, informacion_transaccion):
    if request.method == "GET":
        fecha_query = datetime.datetime.strptime(fecha_peticion, "%Y-%m-%d")
        dataframe_calculo = pd.DataFrame(columns=['fecha', 'acciones', 'valor', 'total'])
        json_informacion = json.loads(informacion_transaccion)
        dataframe_calculo = dataframe_calculo.append(pd.json_normalize(json_informacion), ignore_index=True)
        dataframe_calculo = dataframe_calculo.sort_values(by='fecha')
        fecha_inicio = dataframe_calculo['fecha'][0]
        fecha_inicio = datetime.datetime.strptime(fecha_inicio[:10], "%Y-%m-%d")
        dataframe_calculo = dataframe_calculo.append(dividendos_por_fecha(fecha_query, fecha_inicio), ignore_index=True)
        dataframe_calculo = dataframe_calculo.append(indicador_por_fecha(fecha_query), ignore_index=True)
        dataframe_calculo['fecha'][0] = dataframe_calculo['fecha'][0][:10]
        dataframe_calculo['fecha'] = pd.to_datetime(dataframe_calculo.fecha)
        dataframe_calculo = dataframe_calculo.sort_values(by='fecha')
        dataframe_calculo = calcular_columna_total(dataframe_calculo)
        dataframe_calculo['total'] = dataframe_calculo['total'].astype(float)

        values = get_year_values(dataframe_calculo)

        return HttpResponse(json.dumps({"tir": npf.irr(values)}), content_type='application/json')


def get_year_values(dataframe):
    values = dict()
    count = 0
    for row in dataframe.values:
        if count == 0:
            values['inicio'] = row[3]
        else:
            if row[0].year in values.keys():
                values[row[0].year] += float(row[3])
            else:
                values[row[0].year] = float(row[3])
        count += 1
    array = np.fromiter(values.values(), dtype=float)
    return array


def calcular_columna_total(dataframe):
    total = []
    suma = 0
    for row in dataframe.values:
        if (np.isnan(row[1])):
            total.append(-1 * (suma * row[2]))
        else:
            suma += row[1]
            total.append(row[1] * row[2])

    dataframe['total'] = total
    return dataframe


def indicador_por_fecha(fecha_query):
    query = 'select * from Indicadores where date(fecha)=date(\''+str(fecha_query.date())+'\')'
    df = pd.read_sql(query, connection)
    df = df.rename(columns={'Valor': 'valor'})
    return df


def dividendos_por_fecha(fecha_query, fecha_inicio):
    query = 'select * from Dividendos where date(fecha) between date(\''+str(fecha_inicio.date())+'\') and date(\''+str(fecha_query.date())+'\')'
    df = pd.read_sql(query, connection)
    return df
