#!/usr/bin/env bash
# This tags and uploads an image to Docker Hub

#Assumes this is built
#docker build --tag=mlapi .


dockerpath="dockers/mlapi"

# Authenticate & Tag
echo "Docker ID and Image: $dockerpath"
docker login &&\
    docker image tag mlapi $dockerpath

# Push Image
docker image push $dockerpath 
