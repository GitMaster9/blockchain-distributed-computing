# iExec Bellecour
This directory has instructions on how to use the iExec platform as a requester and a provider using iExec's Bellecour testnet.

You can register an iExec workerpool and add workers to the pool. To manage a workerpool you need to set up a workerpool scheduler (``scheduler-core`` subdirectory).
Then you can add a worker to the workerpool and request a task (as the requestor) to be executed on that workerpool.

### Steps
1. Go to ``scheduler-core`` subdirectory to set up the workerpool and its scheduler.
2. Go to ``worker`` subdirectory and follow the instructions there to add workers to the pool.
3. Go to ``requester`` subdirectory and follow the instructions there to request a task. You can create your own Docker image (``requester/build-docker-image``) to be executed on the iExec platform.

NOTE: ``requester-python-app`` is deprecated.