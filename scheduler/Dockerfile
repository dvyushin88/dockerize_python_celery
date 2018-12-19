FROM python:3.6-alpine

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV INPUT_FOLDER /scheduler/input
ENV OUTPUT_FOLDER /scheduler/output

COPY . /scheduler
WORKDIR /scheduler

RUN pip install -r requirements.txt
