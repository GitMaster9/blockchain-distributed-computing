# Django web server

To test the simulation in a Django web server, you can try running it locally.

To install the needed Python packages run:
```bash
pip install -r requirements.txt
```

Go to the ``app`` directory and run:
```bash
python manage.py runserver
```

### References
- https://docs.golem.network/docs/creators/tools/gvmkit/converting-docker-image-to-golem-format
- https://docs.golem.network/docs/creators/tools/gvmkit/gvmkit-build-installation

### Tutorial

1. From the ``webserver`` directory, build the Docker image:
```bash
docker build -t golem-image .
```

You can test your Docker image by running the Django web server in a Docker container on port 8000.
```bash
docker run -d -p 8000:8000 golem-image
```

4. Convert the Docker image into a Golem image.
```bash
gvmkit-build golem-image --push --nologin
```

5. Save the generated image hash (``image link`` value). Example:
```txt
-- image link (for use in SDK): 18901b10914cabab1d0ca3495b3dfeac182c28e9d90651df682233f1
```
