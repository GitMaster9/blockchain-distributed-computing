# Dapp (Decentralized applications)

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