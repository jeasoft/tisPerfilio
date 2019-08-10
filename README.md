# Creando API REST con Django Rest Framework

Este es el código fuente utilizado para la charla con el título dada en el evento [Technology Innovation Summit](https://tis-conf.dev/).

## Requerimientos
Para ejecutar el código fuente necesitarás lo siguiente:

- Python 3.7
- Internet
- Git 

## Ejecutar el Proyecto

Luego de tener Python instalado e instalado en el PATH, solamente debemos ejecutar lo siguiente:

- Abrir la consola (bash/zsh/cmd/PowerShell).
- Clonar el proyecto.
- Crear Virtual Environment.
- Instalar las dependencias.
- Realizar las migraciones del proyecto
- Crear superusuario
- Lanzar servidor de desarrollo
- y Voila, abrir el navegador en localhost:8000/admin
```
git clone https://github.com/jeasoft/tisPerfilio
cd tisPerfilio
python -m venv env 

(En Windows):
env\Scripts\activate

(En Linux)
source env/bin/activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser 
python manage.py runserver
```

Los enlaces para la parte administrativa:
http://localhost:8000/admin

Los enlaces para ver el API:
http://localhost:8000/api


Saludos!
