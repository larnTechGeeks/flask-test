FROM python:3.9.5-slim

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

# copy every content from the local file to the image
COPY ./src /app

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# configure the container to run in an executed manner
ENTRYPOINT [ "python3" ]

CMD ["app.py"]