FROM service-os-ubuntu-docker.artifactory.si.francetelecom.fr/ubuntu:18.04-minimal

RUN apt-get update && \
    apt install -y python3 python3-pip && \
    apt-get clean


RUN mkdir -p /app/simpleapp/templates
COPY requirements.txt /app/
RUN pip3 install -r /app/requirements.txt

COPY simpleapp/* /app/simpleapp/
COPY simpleapp/templates/* /app/simpleapp/templates/

ENV PYTHONPATH=/app/
CMD python3 /app/simpleapp/front.py
