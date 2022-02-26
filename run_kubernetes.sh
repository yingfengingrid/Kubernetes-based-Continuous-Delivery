#!/usr/bin/env bash

dockerpath="dockers/mlapi"

# Run in Docker Hub container with kubernetes
kubectl run mlapi\
    --generator=run-pod/v1\
    --image=$dockerpath\
    --port=80 --labels app=mlapi

# List kubernetes pods
kubectl get pods

# Forward the container port to host
kubectl port-forward mlapi 8000:80



