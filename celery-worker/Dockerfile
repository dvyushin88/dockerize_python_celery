FROM python:3.6-alpine

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV INPUT_FOLDER /celery-worker/input
ENV OUTPUT_FOLDER /celery-worker/output

COPY . /celery-worker
WORKDIR /celery-worker

RUN pip install -r requirements.txt
