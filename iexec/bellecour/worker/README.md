# Worker tutorial

1. Make sure you are in the "worker" directory
```bash
cd worker
```

1. Initialize iexec workspace
```bash
iexec init --skip-wallet
```

2. Check "chain.json" (default has to be set to "bellecour")
```json
{
  "default": "bellecour",
  "chains": {
    "mainnet": {},
    "bellecour": {}
  }
}
```

3. Create iexec wallet (you will need to input a new password, e.g. "password123worker")
```bash
iexec wallet create --keystoredir ./
```

4. Rename the newly created wallet (e.g. "worker_wallet.json")

5. Update the .env file to match your wallet filename, password and workerpool address

6. Start the Docker container.
```bash
docker compose up -d
```

7. You should now see the worker added to the workerpool on the Grafana GUI and the other metrics endpoints