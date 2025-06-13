# Build Golem Image

1. go to ``requestor/build-golem-image`` directory.
```bash
cd requestor/build-golem-image
```

2. Build the Docker image.
```bash
docker build -t golem-image .
```

You can test your Docker image using the interactive bash terminal (without using bash, the container finishes execution and stops).
```bash
docker run -it golem-image bash
```

4. Convert the Docker image into a Golem image.
```bash
gvmkit-build golem-image --push --nologin
```

5. Save the generated image hash (``image link`` value). Example:
```txt
-- image link (for use in SDK): 18901b10914cabab1d0ca3495b3dfeac182c28e9d90651df682233f1
```
