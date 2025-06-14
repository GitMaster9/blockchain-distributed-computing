# Golem Requestor
Golem Network used Golem images for task execution. You can use public Golem images or build your own by building a Docker image and then converting it into a Golem image using Golem CLI tools (instructions are in the ``build-golem-image`` directory).

### Tutorial
1. Set the ``imageHash`` property in the ``index.mjs`` file (use the generated image hash if you built your own Golem image).

2. Start a ``yagna`` service. First export the ``try_golem`` development app key.
```bash
export YAGNA_AUTOCONF_APPKEY=try_golem
```

Then start the ``yagna`` service:
```bash
yagna service run
```

First time you will need to add funds to the testnet account. Open another terminal and run the following command to complete the configuration:
```bash
yagna payment fund
```

3. You can now start the requestor task (while ``yagna`` is running in the first terminal) by executing the ``index.mjs`` file.
```bash
node index.mjs
```