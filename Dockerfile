FROM python:3.9


ENV PYHTHONDONTWHRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/KarmanaAKM

COPY  . /usr/src/KarmanaAKM

RUN pip install -r /usr/src/KarmanaAKM/requirements/requirements.txt

EXPOSE 8000

COPY docker-entrypoint.sh /usr/src/KarmanaAKM/start-django
RUN chmod +x start-django
RUN chmod -R 777 /usr/src/KarmanaAKM/static

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "collectstatic"]

# run entrypoint.sh
#ENTRYPOINT ["/start-django"]