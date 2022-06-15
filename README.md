# Argo Rollouts Test App 

## docker image build
docker build -t germanx/app:95 . 
docker push germanx/app:95

## Deploy to k8s
kubectl apply -f app-deploy.yaml


## Argo Rollouts Dashboard
kubectl argo rollouts dashboard
http://localhost:3100/rollouts


### Status
kubectl argo rollouts get rollout app
kubectl argo rollouts status app
