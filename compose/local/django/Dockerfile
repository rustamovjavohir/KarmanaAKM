FROM python:3.9


ENV PYHTHONDONTWHRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG BUILD_ENVIRONMENT=local

# Create the app directory Set the working directory
RUN mkdir /app
WORKDIR /app
RUN apt-get update && apt-get install -y siege
RUN apt-get install binutils libproj-dev gdal-bin -y

RUN addgroup --system django \
    && adduser --system --ingroup django django

# Install dependencies
COPY ./requirements /app/
RUN pip install --no-cache-dir -r ${BUILD_ENVIRONMENT}.txt

# Copy the rest of the application code
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

USER root

COPY ./compose/local/django/start.sh /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start
RUN chmod -R 777 /app/static

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


