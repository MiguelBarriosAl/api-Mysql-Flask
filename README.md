# api-mysql-flask

En el momento que se ejecuta el programa revisa si existe, y en caso de que no exista lo cread con los datos de prueba
sqlite3 database.db

Middleware desarrollado para llamada de función antes de acceder a base de datos. Las variables que permiten acceder
según que usuario se registran en .env

curl -u Miguel:Barrios http://localhost:5000/count