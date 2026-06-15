# Prueba Citas de Entrega

## Descripción proyecto

Sistema fullstack para la gestión de citas de entrega de mercancía en retail textil.

## Tecnologías

### BackEnd

- Django
- Django REST Framework
- PostgreSQL
- JWT
- Swagger

### Instalación backend

 1. Activar el ambiente de desarrollo
 `python -m venv venv`

 2. Instalar las dependencias
 `pip install -r requirements.txt`

 3. Variables de entorno
    Ejemplo .env

    SECRET_KEY=""
    DEBUG=True

    DB_NAME=""
    DB_USER=""
    DB_PASSWORD=""
    DB_HOST=""
    DB_PORT=""

### Migraciones

ejecute las migraciones
 `python manage.py migrate`

### Ejecutar servidor

para correr el servidor local ejecute el comando
 `python manage.py runserver`

### Documentación API

- Swagger UI: `http://localhost:8000/api/docs/`
- Redoc UI: `http://localhost:8000/api/redoc/`
