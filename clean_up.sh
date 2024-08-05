#!/bin/bash

# Detener todos los contenedores en ejecución
docker stop $(docker ps -q)

# Eliminar todos los contenedores
docker rm $(docker ps -a -q)

# Eliminar todas las imágenes
docker rmi -f $(docker images -q)
