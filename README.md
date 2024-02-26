# Bitácora
 Proyecto de facilita la gestión de los registros de tareas realizadas por distintos usuarios dentro de una bitácora. 
 
 Se trata de un CRUD simple realizado en Django, incorporando su sistema de autenticación y autorización.

 ## Pre requisitos
 - Django 5.0 soporta Python 3.10, 3.11, y 3.12
 - Virtualenv o similar

## Instalación
1. Crear entono virtual: 
``` python -m venv venv ```

2. Activar el entorno virtual:
```venv\Scripts\activate ```

3. Instalar dependencias:
``` pip install -r requirements.txt ``` 

4. Generar los scripts para crear las migraciones (BD):
``` python manage.py makemigrations ``` 

5. Aplicar las migraciones en la BD:
```  python manage.py migrate ``` 

6. Crear super usuario para acceder al /admin/
``` python manage.py createsuperuser```

7. Levantar un servidor local para servir la aplicación en el localhost:8000
``` python manage.py runserver``` 

## Pantallas
### Login
![image](https://github.com/mariana-git/Bitacora/assets/88113403/a9023fc7-3ee8-4870-914a-e94ca6f47d7a)
### Listado
![image](https://github.com/mariana-git/Bitacora/assets/88113403/dd545bde-d9a1-47ef-8714-0a8c70615dda)
### Creación
![image](https://github.com/mariana-git/Bitacora/assets/88113403/a72bcff4-8348-4515-8e1b-209e145251f4)
### Menú
![image](https://github.com/mariana-git/Bitacora/assets/88113403/b5e44f4b-1c06-4bb9-8b75-8838bebceb40)


