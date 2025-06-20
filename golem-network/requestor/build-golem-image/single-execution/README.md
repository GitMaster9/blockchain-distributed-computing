# Build Golem Image - single execution

### References
- https://docs.golem.network/docs/creators/tools/gvmkit/converting-docker-image-to-golem-format
- https://docs.golem.network/docs/creators/tools/gvmkit/gvmkit-build-installation

### Tutorial

1. go to ``single-execution`` directory.
```bash
cd single-execution
```

2. Build the Docker image.
```bash
docker build -t golem-image .
```

You can test your Docker image using the interactive bash terminal (without using bash, the container finishes execution and stops).
```bash
docker run -it golem-image bash
```

3. Install ``gvmkit-build`` Python package:
```bash
pip install gvmkit-build
```

4. Convert the Docker image into a Golem image.
```bash
gvmkit-build golem-image --push --nologin
```

5. Save the generated image hash (``image link`` value). Example:
```txt
-- image link (for use in SDK): 18901b10914cabab1d0ca3495b3dfeac182c28e9d90651df682233f1
```
