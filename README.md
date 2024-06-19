# Proyecto BD

Este proyecto utiliza Docker y Docker Compose para crear un entorno de desarrollo para una aplicación Django.

## Prerrequisitos

Asegúrate de tener instalados los siguientes software en tu sistema:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Instrucciones

Sigue estos pasos para levantar el contenedor con Django utilizando Docker Compose.

### 1. Clonar el repositorio

Primero, clona este repositorio en tu máquina local:

git clone https://github.com/pabloMBDTF/Proyecto_BD.git
cd Proyecto_BD

### 2. Levantar el contenedor

Situate en la raiz del proyecto, luego pon el siguiente comando:

docker-compose up --build

### 3. Crear SuperUser

Accede a la terminal del proyecto docker y coloca el siguiente comando:

python manage.py createsuperuser
