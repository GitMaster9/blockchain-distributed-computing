# Golem-Workers
Golem-Workers are a high-level API for providing access to GPU and CPU resources on the Golem Network. It uses HTTP calls and JSON files to create clusters and add nodes that execute tasks on the provider nodes on the Golem Network.

Golem-Workers is a Python web server accompanied by golem-node (also called yagna) service - the component responsible for communicating with the Golem Network.

### References
- https://docs.golem.network/docs/creators/golem-workers
- https://docs.golem.network/docs/creators/golem-workers/hello-example
- https://github.com/golemfactory/golem-workers

### Steps
1. Start the docker containers.
```bash
docker compose up -d --build
```

Now you should be able to see the golem-workers endpoints:
- http://localhost:8000
- http://localhost:8000/docs
- http://localhost:8000/redoc

2. Create a Cluster with the ``create-cluster.json`` file:

```bash
curl --location 'http://localhost:8000/create-cluster' \
--header 'Content-Type: application/json' \
--data @create-cluster.json
```

3. Create a Node with the ``create-node.json`` file:

```bash
curl --location 'http://localhost:8000/create-node' \
--header 'Content-Type: application/json' \
--data @create-node.json
```

You can now get the cluster's status with the generic ``cluster.json`` file.
```bash
curl --location 'http://localhost:8000/get-cluster' \
--header 'Content-Type: application/json' \
--data @cluster.json
```

4. Access the Hello Service. Once the node is started, open your browser and navigate to http://localhost:8080. You should see the message Hello displayed.

5. You can stop the Node with the generic ``node.json`` file:
```bash
curl --location 'http://localhost:8000/delete-node' \
--header 'Content-Type: application/json' \
--data @node.json
```

6. When you are done, you can stop the Cluster with the ``cluster.json`` file:
```bash
curl --location 'http://localhost:8000/delete-cluster' \
--header 'Content-Type: application/json' \
--data @cluster.json
```