# K8s_ASGMT

# Task 1
```
1. When running an application, its best to make a new directory or a new folder to store all of your application files in an organized place. After knowing where your files are located in your system, open the Command Prompt or Terminal.

2. use the cd to go into the 
 
3. Create a Dockerfile:

FROM python:3.10
COPY ./requirements.txt requirements.txt
COPY templates/ /templates/
RUN pip install -r requirements.txt
COPY application.py application.py
ENV FLASK_APP=application.py
EXPOSE 5000
CMD flask run --host=0.0.0.0

4. By using the Dockerfile, use it to build an image with the command:
    "sudo docker build -t ------" 
   * ----- is the name that can be given to the newly created image. I named my image fproject1.1
    
    
5. sudo docker run -d -p 5000:5000 ------ 

```

# Task 2
1. a

2.

