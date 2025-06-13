# Golem Requestor tutorial

1. Build the Golem image (use the ``build-golem-image`` directory).

2. Edit the ``imageHash`` property in the ``index.mjs`` file. Use the generated image hash when building the Golem image.

3. Start a Yagna service. First export the ``try_golem`` development app key.
```bash
export YAGNA_AUTOCONF_APPKEY=try_golem
```

Then start the yagna service:
```bash
yagna service run
```

First time you will need to add funds to the testnet account. Open another terminal and run the following command to complete the configuration:
```bash
yagna payment fund
```

4. You can now start the requestor task (while yagna is running in the first terminal) by executing the ``index.mjs`` file.
```bash
node index.mjs
```