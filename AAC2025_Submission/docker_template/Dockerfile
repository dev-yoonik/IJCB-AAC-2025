FROM python:3.9.16-slim-buster

WORKDIR /challenge
COPY ./requirements.txt /challenge/requirements.txt

RUN pip install --no-cache-dir -r /challenge/requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY . /challenge/.

ARG HOST_DOMAIN=0.0.0.0
ARG PORT_NUMBER=7007

ENV HOST_DOMAIN=${HOST_DOMAIN}
ENV PORT_NUMBER=${PORT_NUMBER}

EXPOSE ${PORT_NUMBER}

CMD uvicorn main:app --host=$HOST_DOMAIN --port=${PORT_NUMBER}
