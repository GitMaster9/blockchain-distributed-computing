# Ray on Golem API

Ray on Golem is a special Python workflow of executing tasks on Golem Network based on Ray, a parallelization framework in Python.

NOTE: This tutorial is still in development.

### References
- https://docs.golem.network/docs/creators/ray/quickstart
- https://github.com/golemfactory/ray-on-golem
- https://www.youtube.com/watch?v=IneVyiVdMKQ

### Tutorial
1. Start the ``yagna`` service in one terminal.
```bash
yagna service run
```

2. Open another terminal and start the ray cluster using a cluster configuration file.
```bash
ray up golem-cluster.yaml --yes
```

You can download the example golem-cluster.yaml file here:
```bash
wget https://ray.golem.network/golem-cluster.yaml
```

3. Submit your Python script to be executed on your cluster.
```bash
ray submit golem-cluster.yaml simple-task.py
```

You can download the example golem-cluster.yaml file here:
```bash
wget https://github.com/golemfactory/ray-on-golem/raw/main/examples/simple-task.py 
```

4. You can stop the cluster with:
```bash
ray down golem-cluster.yaml --yes
```

5. To stop all Ray on Golem componts use:
```bash
ray-on-golem stop
```