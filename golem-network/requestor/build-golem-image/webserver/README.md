# Django web server

To test the simulation in a Django web server, you can try running it locally.

To install the needed Python packages run:
```bash
pip install -r requirements.txt
```

Go to the ``app`` directory and run it as a Django development server:
```bash
python manage.py runserver
```

You can also run it as a uvicorn server:
```bash
uvicorn myproject.asgi:application --host 0.0.0.0 --port 8000
```

### References
- https://docs.golem.network/docs/creators/tools/gvmkit/converting-docker-image-to-golem-format
- https://docs.golem.network/docs/creators/tools/gvmkit/gvmkit-build-installation

### Tutorial

1. From the ``webserver`` directory, build the Docker image:
```bash
docker build -t golem-image-webserver .
```

You can test your Docker image by running the Django web server in a Docker container on port 8000.
```bash
docker run -d -p 8000:8000 golem-image-webserver
```

2. Install ``gvmkit-build`` Python package:
```bash
pip install gvmkit-build
```

3. Convert the Docker image into a Golem image.
```bash
gvmkit-build golem-image-webserver --push --nologin
```

4. Save the generated image hash (``image link`` value). Example:
```txt
-- image link (for use in SDK): 54974f71ab794a1298b23ba19a872eace9b7e353298bdb91d05a627a
```
