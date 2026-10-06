FROM python:3.12-slim

WORKDIR /services

COPY ./requirements.txt /services

RUN  pip install -r requirements.txt

COPY . /services

CMD python services/producer && python services/consumer

