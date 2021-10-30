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

3. To make a requirements.txt, enter the command on your computer or virtual environment to run the application:
py -m pip list (Windows)
python -m pip list (Unix/MacOS)

This shows what packages will be needed to be installed to run your application. Copy the list of packages and paste it
into a new file called 'requirements.txt'.  

To make a new file by using the command line in the same directory where the application files are located, enter
the command "nano requirements.txt" and a blank screen should show up. It is also possible to paste and then save 
the list package information by using this method too. 

By listing the needed packages, the Dockerfile can be told to read the package information and download it to make 
an image to run the application. 

*The naming of 'requirements.txt' is case sensitive and should be written as shown in quotes. 
 
4. To create a Dockerfile in the same directory where the application files are located, enter the following:

FROM python:3.10
COPY ./requirements.txt requirements.txt
COPY templates/ /templates/
RUN pip install -r requirements.txt
COPY application.py application.py
ENV FLASK_APP=application.py
EXPOSE 5000
CMD flask run --host=0.0.0.0

From the command line in the same application files directory, you can also run 'nano Dockerfile' and paste the following 
information above and it should look like as shown below if the terminal was used to make the Dockerfile. 
```

<html>
   <h1>
      <img style="float: center;" src=14.png width="1000" />
   </h1>
</html>

<html>
   <h1>
      <img style="float: center;" src=2.png width="1000" />
   </h1>
</html>

5. By using the Dockerfile, use it to build an image with the command:
    "sudo docker build -t ------" 
   * ----- is the name that can be given to the newly created image. I named my image fproject1.1
    
    
6. sudo docker run -d -p 5000:5000 ------ 

```

# Task 2
1. a

2.

