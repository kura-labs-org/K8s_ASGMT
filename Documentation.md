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

This Dockerfile will take a python3 image and download the necessary dependencies and finally run the flask app, ultimately constructing the image we desire. Use `docker build -t <image name>:<image tag> .` to build the image and `docker push <image name>:<image tag>` to push it to Dockerhub.

### Step 2: Deploying into a K8s Cluster

