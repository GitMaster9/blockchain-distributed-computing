# Blockchain based Distributed computing
This is the main repository for my Master's thesis on blockchain based distributed computing. It has code and tutorials on how to use some of the tools on the Golem Network and iExec platforms.

### Requestor node
I wrote a Monte Carlo simulation of a simplified 1D Photon Radiation Transport using Python scripts to be used as an example of task execution that are requested by the requestor nodes and run on the provider nodes. The scripts can use different simulation parameters to mimic task parallelization on multiple machines as a form of distributed computing. Both Golem and iExec use the scripts in a Docker image but have small differences only in saving the result output.

### Provider node
There are instructions to set up your machine as a (resource, machine) provider on both Golem and iExec platforms in their own subdirectories. For both platform a free and public testnet is used but requestor nodes can use specific provider nodes if needed.

### References
- https://docs.golem.network/
- https://www.iex.ec/
- https://tools.docs.iex.ec/