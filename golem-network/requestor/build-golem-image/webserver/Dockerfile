FROM python:3.11-slim

WORKDIR /golem/app
VOLUME /golem/tmp

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /golem/app

EXPOSE 8000

ENTRYPOINT ["uvicorn", "myproject.asgi:application", "--host", "0.0.0.0", "--port", "8000"]