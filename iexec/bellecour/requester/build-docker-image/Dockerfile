FROM python:3.11-slim

WORKDIR /iexec

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY radiation_transport.py /iexec/radiation_transport.py
COPY main.py /iexec/main.py

ENTRYPOINT ["python3", "/iexec/main.py"]