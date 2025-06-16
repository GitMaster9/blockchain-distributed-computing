# JS API

### References
- https://docs.golem.network/docs/quickstarts/js-quickstart

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