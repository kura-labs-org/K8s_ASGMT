FROM python:3.9.7-slim-buster

RUN mkdir /python_app

WORKDIR /python_app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "application.py"]

EXPOSE 5000

