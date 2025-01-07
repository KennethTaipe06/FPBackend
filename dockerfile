# Usa una imagen oficial de Python como base
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias al contenedor
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el script wait-for-it
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Copia todo el proyecto al contenedor
COPY . .

# Expon la aplicación en el puerto 8000
EXPOSE 8000

# Ejecuta el servidor de desarrollo de Django
CMD ["/wait-for-it.sh", "db:3306", "--", "python", "backend/manage.py", "runserver", "0.0.0.0:8000"]
