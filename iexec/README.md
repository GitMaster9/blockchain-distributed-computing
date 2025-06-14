# iExec
This directory has instructions on how to use the iExec platform as a requester and a provider using iExec. In theory, you could start a private blockchain and use it to connect requesters and providers but that is still in development and current instructions are limited (``private-blockchain`` subdirectory). For now use the ``bellecour`` subdirectory to set up requesters and providers on the Bellecour testnet.

Also, you can add a worker to the workerpool and request a task to be executed on that workerpool.

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
3. Go to "bellecour/requester" directory and follow the instructions