# K8s Assignment
### Objectives
**We wish to take a flask app and create and push an image of it to Dockerhub. We then want to deploy that app in a K8s cluster.**

### Step 1: Dockerizing the Flask App
First we want to create a Dockerfile and place it in the root of the flask app. Here is such a Dockerfile.

```
FROM python:3.10
WORKDIR /home
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /home
ENV FLASK_APP=application.py

ENTRYPOINT flask run --host=0.0.0.0
```

This Dockerfile will take a python3 image and download the necessary dependencies and finally run the flask app, ultimately constructing the image we desire. Use `docker build -t <image_name>:<image_tag> .` to build the image and `docker push <image_name>:<image_tag>` to push it to Dockerhub.

### Step 2: Deploying into a K8s Cluster

Let's create our kubernetes cluster! `k3d create cluster <cluster_name> -p 8081:8080@loadbalancer` This command will also expose the connect the 8081 port to the loadbalancer's 8080. All that is left is to deploy our app. `kubectl create -f deploy_flask.yml` Let's take a closer look at this yml file.

```
# Helloworld application- just the deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: scanning-deployment
spec:
  selector:
    matchLabels:
      app: scanning-app
  replicas: 1 # tells deployment to run 1 pods matching the template
  template: # create pods using pod definition in this template
    metadata:
      labels:
        app: scanning-app
    spec:
      containers:
      - name: scanning-app-container
        image: srkodes/scan_proj:latest
        ports:
        - containerPort: 5000
---
apiVersion: v1
kind: Service
metadata:
  name: scanning-app-service
spec:
  type: LoadBalancer
  ports:
  - port: 8080
    protocol: TCP
    targetPort: 5000
  selector:
    app: scanning-app
```

It's important to note the various ports. The container is exposing 5000, because that is where flask apps can be accessed. The Loadbalancer takes incoming traffic on port 8080, and reroutes it to 5000. This allows traffic from 8081 to reach 5000, where our flask app can be accessed.