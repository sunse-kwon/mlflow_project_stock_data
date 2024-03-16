FROM python:3.11.4-slim

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apt-get update && apt-get -y upgrade \
    && pip install --upgrade pip \
    && pip --version

RUN pip install --no-cache-dir -r requirements.txt \
    && rm requirements.txt


# COPY ./mlflow /mlflow
# WORKDIR /mlflow


