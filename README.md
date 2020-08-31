# Tasa Interna Retorno
## Presentado por Juan Felipe Alfonso Avila

<br>
Proyecto desarrollado en Django con Python version 3.6,
con base de datos sqlite 3 en el cual se ubican los Dividendos
e Indicadores para realizar el cálculo de la tasa interna de retorno
según lo solicitado. Para la ejecución del web Service se necesitan
las librerias ubicadas en el archivo requirements.txt

<br>
<br>
Para desplegar el servicio hay que ejecutar
<br>
python manage.py runserver localhost:8000

<br><br>
Para hacer el llamado del servicio se debe generar un GET request, que,
según lo solicitado será con la siguiente URL
<br>
localhost:8000/getServerState/2020-05-05/[{"fecha":"2019-01-01", "acciones":100, "valor":109},{"fecha":"2019-05-20", "acciones":500, "valor":107},{"fecha":"2019-10-06", "acciones":-300, "valor":109},{"fecha":"2020-02-22", "acciones":-100, "valor":110}]
<br>
Que podrá cambiar según los datos que se le ingresen al sistema