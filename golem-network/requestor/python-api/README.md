# Python API

### Python version
Currently the latest Python version that is tested and working in the requestor script is 3.10.13. Create a Python virtual environment with this version and then use it to execute the script.

### References
- https://docs.golem.network/docs/quickstarts/python-quickstart

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

3. Generate the yagna app key.

```bash
yagna app-key create requestor
```

This should produce a 32-character-long hexadecimal app key that you need to note down as it will be needed to run the requestor agent.

```bash
export YAGNA_APPKEY=insert-your-32-char-app-key-here
```

Example:
```bash
export YAGNA_APPKEY=a67eb7a9e906414680b9338f42445501
```

4. You can now start the requestor task (while ``yagna`` is running in the first terminal) by executing the ``main.py`` file.
```bash
python main.py
```