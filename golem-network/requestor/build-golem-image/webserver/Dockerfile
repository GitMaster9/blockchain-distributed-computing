FROM python:3.11-slim

WORKDIR /golem/app
VOLUME /golem/tmp

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /golem/app

# Expose the port Django runs on
EXPOSE 8000

# Default command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]