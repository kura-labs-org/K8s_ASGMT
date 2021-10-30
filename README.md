# K8s_ASGMT

# Task 1
```
1. When running an application, its best to make a new directory or a new folder to store all of 
   your application files in an organized place separated from other computer files. As shown 
   below, I made a new folder called "project" on my Desktop to store all of my application 
   files in a one place.
```

<html>
     <h1>
        <img style="float: center;" src=12.png width="1000" />
     </h1>
</html>  

<html>
   <h1>
      <img style="float: center;" src=13.png width="1000" />
   </h1>
</html>
```
2. After knowing where your files are located in your system, open the Command Prompt or Terminal. 
Now open use the cd command to enter into the directory. As shown above I have two files called
"Dockerfile" and requirements.txt. To run an application on Docker, these two files are needed. 
```

3. 

 
4. To create a Dockerfile enter the following:

FROM python:3.10
COPY ./requirements.txt requirements.txt
COPY templates/ /templates/
RUN pip install -r requirements.txt
COPY application.py application.py
ENV FLASK_APP=application.py
EXPOSE 5000
CMD flask run --host=0.0.0.0

5. By using the Dockerfile, use it to build an image with the command:
    "sudo docker build -t ------" 
   * ----- is the name that can be given to the newly created image. I named my image fproject1.1
    
    
6. sudo docker run -d -p 5000:5000 ------ 

```

# Task 2
1. a

2.

