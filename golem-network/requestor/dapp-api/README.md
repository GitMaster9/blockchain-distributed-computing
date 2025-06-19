# Dapp (Decentralized applications)
A dApp (decentralized application in the context of Golem) is a new way of deploying applications on the Golem Network. It is still in early access and should be considered experimental. It is a method of deploying a full application (website or a public API) by combining services and resources within the network to run the entire app on the Golem Network (e.g. frontend, backend API server, database).
You can use ``dapp-runner``, a simple one-command CLI tool, or ``dapp-manager``, CLI with more features and options.

### dapp-runner
1. Open a terminal and run the ``yagna`` service:
```bash
yagna service run
```

2. Create a new Python virtual environment and install ``dapp-runner``:
```bash
pip install -U pip dapp-runner
```

3. Open another terminal and start the dapp using:
```bash
dapp-runner start --config config.yaml webapp.yaml
```

``config.yaml`` and ``webapp.yaml`` were downloaded from example files by:

```bash
curl https://raw.githubusercontent.com/golemfactory/dapp-store/81e3f50aba90a84d335a26cb9cc2ea778193be11/apps/todo-app.yaml > webapp.yaml
```

```bash
curl https://raw.githubusercontent.com/golemfactory/dapp-runner/main/configs/default.yaml > config.yaml
```

You can now check the example ToDo app on port ``localhost:8080``

### dapp-manager
1. Open a terminal and run the ``yagna`` service:
```bash
yagna service run
```

2. Create a new Python virtual environment and install ``dapp-manager``:
```bash
pip install -U pip dapp-manager
```

3. Open another terminal and start the dapp using:
```bash
dapp-manager start --config config.yaml webapp.yaml
```

This will output the app ID hex string.

You can then check the current state of the dapp console.
```bash
dapp-manager read <the-hex-string> data
```

Example:
```bash
dapp-manager read 1688dbe9b7d84a2fabb71a2bbc555c64 data
```

You can also keep track of it "live" (similar to ``tail``) by adding the ``--follow`` flag.
```bash
dapp-manager read --follow 1688dbe9b7d84a2fabb71a2bbc555c64 data
```

In case something goes amiss, dapp-manager will output: ˙App <the-hex-string> is not running.``

Whatever the reason, you can still query the various streams of a terminated dapp by adding the --no-ensure-alive option, e.g.:
```bash
dapp-manager read <the-hex-string> --no-ensure-alive stderr
```

Example:
```bash
dapp-manager read 1688dbe9b7d84a2fabb71a2bbc555c64 --no-ensure-alive stderr
```

4. You can stop the app by running:
```bash
dapp-manager stop <the-hex-string>
```

Example:
```bash
dapp-manager stop 1688dbe9b7d84a2fabb71a2bbc555c64
```