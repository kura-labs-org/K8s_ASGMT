# K8s_ASGMT

<h1>Goal</h1>

The goal of this deployment was to have a better understanding of doing kubernetes deployments with a more indepth understanding of what can be done to improve security of the deployments and how services interact with one another on a network level

<h2>Instructions</h2>

The assignment instructions were to create a dockerized version of a flask application and then deploy it to a local kubernetes cluster.

<h3> Creating an image. </h3>

For a flask application, you must create a Dockerfile that utilizes the base [python image](https://hub.docker.com/_/python). This will allow you to use the image as a template to deploy the application.

`
FROM python ##change to specific image

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]`

This will allow the Dockerfile to call the image, use the app as working directory, copy and run the pip command for pulling the requirements, following the deployment, the mython command will run flask with host 0.0.0.0. This allows any device on network to access it outside of the localhost.

More to read [here](https://docs.docker.com/language/python/build-images/)

It's important now to [upload this image](https://docs.docker.com/engine/reference/commandline/push/) to Dockerhub as the image must be pulled from Dockerhub or some repository for use in next steps.

<h4> Deployment </h4>

Steps to take:

-Create a cluster using the k3d cluster create command and open the ports 8080:8080. This will allow access from 8080 to a port within the Kubernetes network space on 8080.

-Create a yaml file that would be used to deploy the application. For this one, we can use a yaml that looks like this

```apiVersion: apps/v1

kind: Deployment

metadata:

  name: flask-deployment
  
spec:

  selector:
  
    matchLabels:
    
      app: flask
      
  replicas: 1
  
  template:
  
    metadata:
    
      labels:
      
        app: flask
        
    spec:
    
      containers:
      
      - name: flask
      
        image: flask-image
        
        ports:
        
          - containerPort: 80
          
          
---

apiVersion: v1

kind: Service

metadata:

  name: flask-service
  
spec:

  ports:
  
  - port: 8080
  - 
    targetPort: 80
    
    name: http
    
  selector:
  
    app: flask
    
```

What happens here is the connection between the application through a load balancer on the cluster targeting a service resource that leads to the actual application pod that is running internally in the kubernetes space.

This would look like localhost -->dockers network (load balancer) --> service connector --> internet kubernetes space where 80 is explosing Flask.
