# Usar una imagen base oficial de Python
FROM python:3.12

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de requisitos
COPY requirements.txt /app/

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . /app/

# Exponer el puerto en el que la aplicación correrá
EXPOSE 8000

# Comando para correr la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
