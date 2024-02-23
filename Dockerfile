# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de la aplicación a la imagen del contenedor
COPY . /app

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Expone el puerto 5000 en el contenedor
EXPOSE 5000

# Define el comando por defecto para ejecutar tu aplicación
CMD ["python", "main.py"]