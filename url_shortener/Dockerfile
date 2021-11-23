From python:3.10
WORKDIR /urlshortener
COPY . .
run pip install -r requirements.txt
ENV FLASK_APP=application.py
EXPOSE 5000
CMD flask run --host=0.0.0.0
