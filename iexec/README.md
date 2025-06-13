# Scheduler Core tutorial
This repository is an example of how to set up a private workerpool using iExec. You can use iExec's Bellecour testnet or a private blockchain (in this example a Ganache test chain), they both don't use real tokens. Also, you can add a worker to the workerpool and request a task to be executed on that workerpool.

NOTE: using a private blockchain is still in development

## References
This repository was set up using following documentation sites and repositories:

- https://protocol.docs.iex.ec/for-workers/manage-a-pool-of-workers
- https://github.com/iExecBlockchainComputing/deploy-workerpool
- https://tools.docs.iex.ec/overview/helloWorld/3-buildIApp


## Prerequisites
1. Install Docker, node and npm

2. Install iexec SDK npm packages
```bash
npm install -g iexec
```

For the requestor node, another dependency might be needed
```bash
npm install -g @iexec/iapp
```

## Steps to replicate (Bellecour)
1. Go to "bellecour/scheduler-core" directory and follow the instructions
2. Go to "bellecour/worker" directory and follow the instructions there. You can add multiple workers when you make sure the first worker is added to the workerpool.
3. Go to "bellecour/requester-python-app" directory and follow the instructions