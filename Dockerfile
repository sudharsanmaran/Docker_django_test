FROM python:3.8.10
ENV PYTHONUNBUFFERED 1
#working dir in docker container
WORKDIR /code
#copying event_driven requirements.txt to
#/app/requirements.txt in docker container
COPY requirements.txt /code/
RUN pip install -r requirements.txt
# "." means all the files
COPY . /code
CMD python manage.py runserver 0.0.0.0:8000