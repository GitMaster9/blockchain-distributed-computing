# Scheduler Core tutorial

1. Make sure you are in the "scheduler-core" directory
```bash
cd scheduler-core
```

2. Initialize iexec workspace
```bash
iexec init --skip-wallet
```

3. Import iexec wallet (you will need to input a new password, e.g. "password123core")
```bash
iexec wallet import [privateKey] --keystoredir ./
```

```bash
iexec wallet import 0xb31a1121f4855e0cd32a1633f556174bd8326d47c36eb0b6a866bdf894b7cf50 --keystoredir ./
```

4. Rename the newly imported wallet (e.g. "core_wallet.json")

5. Localy initialize you workerpool registration
```bash
iexec workerpool init --wallet-file "core_wallet.json" --keystoredir ./
```

6. Edit the "iexec.json" and change the "workerpool.description". This field will appear publicly on the blockchain and the marketplace.

7. Make sure the "workerpool.owner" field of iexec.json file matches the "address" field of the "core_wallet.json" file.
```bash
jq .workerpool iexec.json
```

```bash
jq .address core_wallet.json
```

8. Register your workerpool on your private blockchain to get its workerpool address
```bash
iexec workerpool deploy --wallet-file "core_wallet.json" --keystoredir ./ --chain local
```

9. Create a new Docker network (if the scheduler-core containers need to be on the same network as the worker containers)
```bash
docker network create iexec_network
```

10. Update the .env file to match your workerpool address and other parameters

11. Start the Docker containers.
```bash
docker compose up -d
```

12. Check the Grafana dashboard

```
http://$PROD_GRAFANA_HOST/
```

e.g.
```
http://localhost:3000/
```

Various metrics and health endpoints that are exposed by the services:
```
http://$PROD_CHAIN_ADAPTER_HOST/config/chain
```

```
http://$PROD_CHAIN_ADAPTER_HOST/actuator/health
```

```
http://$PROD_CORE_HOST/metrics
```

```
http://$PROD_CORE_HOST/actuator/health
```