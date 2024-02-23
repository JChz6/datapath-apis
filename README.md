# Proyecto de Despliegue de API

Este es un proyecto de ejemplo que demuestra cómo desarrollar una API usando Flask y conectarla a una base de datos PostgreSQL. El proyecto incluye métodos para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en una tabla de películas.

## Requisitos

- Python 3.x
- Docker
- PostgreSQL

## Configuración

Antes de ejecutar la aplicación, asegúrate de tener PostgreSQL en ejecución y configurado con las credenciales adecuadas. Puedes modificar la configuración de la base de datos en el archivo `.env`.

Además, crea un entorno virtual e instala las dependencias del proyecto utilizando el archivo `requirements.txt`.

## Ejecución

Para ejecutar la aplicación localmente, sigue estos pasos:

1. Ejecutar el contenedor de Docker para la aplicación
2. Inicia el contenedor de Docker para PostgreSQL
3. Inicia la aplicación Flask:



La aplicación estará disponible en `http://localhost:5000`.

## Uso

Una vez que la aplicación esté en ejecución, puedes acceder a los siguientes endpoints:

- `GET /movies`: Obtener todas las películas.
- `GET /movies/<id>`: Obtener una película por su ID.
- `POST /movies`: Agregar una nueva película.
- `PUT /movies/<id>`: Actualizar una película existente.
- `DELETE /movies/<id>`: Eliminar una película por su ID.

Puedes probar estos endpoints utilizando Postman.
