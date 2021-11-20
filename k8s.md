# K8s assignment

#### Dockerize your flask app and create an image you can push up to DockerHub. 
### Created a folder in terminal  customapp2

Used git to clone app files

```

$  git clone https://…

```

Deleted files: README.md, LICENSE, and Pictures

```
Nano application.py
```

Updated the code : added host in code below

 if __name == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
    

To make sure the requirements are updated cat the requirement.txt file

```
cat requirements.txt

```
Then install flask
```
pip install flask

```
```
Nano Dockerfile

FROM python:3.9.10 ( The specific version of python needed to run application)

COPY ./requirements.txt requirements.txt (we want to take the requirements.txt and add it to the current directory)

RUN pip install -r requirements.txt (using this command to run the code to install the needed items from the requirements.txt file)

COPY application.py application.py (we want to bring the application.py over as well)

COPY static/ /static/

COPY templates/ /templates/

ENV FLASK_APP=application.py (we are creating the environment so we can run the application

EXPOSE 5000 (here we are exposing the 5000 so we can access via the web)

CMD flask run --host=0.0.0.0

Run ---> $ docker build -t customapp2:latest .
```
( At the end of the run command add the directory you want the docker file to run in if you want the dockerfile to run the current directory add . to the end of the line of code.
Run the container ---> $ docker run -d -p 5000:5000 customapp2
$ docker ps -a
$ docker exec -it docker exec -it 9d833d308c61 bash
For some reason this command will only work when I use the container ID


Now you are in the container, run the curl command to test the application
```
root@96081e83a270:/# curl localhost:5000
```
To check if it is running, open a web browser and type localhost:5000 then hit enter.
It should be successful.

 Deploy your Flask app in Kubernetes.

Now, recreate the previous image and tag it 
```
docker build -t 32322323/customapp2:latest .
```

Push it to dockerhub
```
docker push 32322323/customapp2:latest
```
Create your cluster with a Load Balancer
```
k3d cluster create -p “8081:8080@loadbalancer”
```
Create a pod

```
kubectl run --image 32322323/customapp2 -it customapp2
```
Create a deployment yaml file for your flask app.

```
kubectl apply -f customapp2.yml
``` 
Check web browser

http://localhost:8080
