# Worker tutorial

1. Make sure you are in the "worker" directory
```bash
cd worker
```

2. Initialize iexec workspace
```bash
iexec init --skip-wallet
```

3. Import iexec wallet (you will need to input a new password, e.g. "password123worker")
```bash
iexec wallet import [privateKey] --keystoredir ./
```

```bash
iexec wallet import 0x31e19c19f300ff734831eba61282cbe7062f1580f762c9cf6a6f395dcdd7b616 --keystoredir ./
```

4. Rename the newly imported wallet (e.g. "worker_wallet.json")

5. Update the .env file to match your wallet filename, password and workerpool address

6. Start the Docker container.
```bash
docker compose up -d
```

7. You should now see the worker added to the workerpool on the Grafana GUI and the other metrics endpoints