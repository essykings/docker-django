FROM python:3
ADD requirements.txt /src/
RUN cd /src && pip install -r requirements.txt

ADD . /src/
WORKDIR /src


CMD python manage.py collectstatic ;python manage.py migrate;  gunicorn my_django18_project.wsgi -b 0.0.0.0:8000 

EXPOSE 8000



