# Build iExec Docker image
You can build your own Docker image to be executed on the iExec provider (worker) nodes.

### Tutorial

1. Go to ``requester/build-docker-image`` directory.
```bash
cd requester/build-docker-image
```

2. Build the Docker image with a tag argument so it can be published as a public image on the Docker Hub repository.
```bash
docker build -t your-docker-username/iexec-image-name:1.0 .
```

Example:
```bash
docker build -t sheyoindustries/iexec-requestor:1.0 .
```

3. Push the Docker image to Docker Hub.
```bash
docker push your-docker-username/iexec-image-name:1.0
```

If you have trouble pushing the image to Docker Hub, use this link to generate a Personal Access Token

- https://tools.docs.iex.ec/overview/helloWorld/3-buildIApp#%F0%9F%9A%80-deploy-your-iapp

Now you can use your Docker image as a task to be executed on the iExec platform.