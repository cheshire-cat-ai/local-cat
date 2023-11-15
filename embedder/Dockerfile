FROM python:3.10.11-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app
COPY . /app

RUN apt-get -y update && apt-get install -y build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app

RUN pip install -U pip && \
    pip install -r ./requirements.txt
CMD python main.py