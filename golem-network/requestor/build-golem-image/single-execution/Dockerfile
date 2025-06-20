FROM python:3.11-slim

WORKDIR /golem/tmp
VOLUME /golem/tmp

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY radiation_transport.py /golem/radiation_transport.py
COPY main.py /golem/main.py