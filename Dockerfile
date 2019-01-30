FROM ubuntu:18.04

RUN apt-get update && \
    apt install -y python3 python3-pip && \
    apt-get clean


RUN mkdir -p /app/simpleapp
COPY requirements.txt /app/
RUN pip3 install -r /app/requirements.txt

COPY simpleapp/* /app/simpleapp/

ENV PYTHONPATH=/app/
CMD python3 /app/simpleapp/front.py
