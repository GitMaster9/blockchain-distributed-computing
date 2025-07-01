# Scheduler Core

### References
This repository was set up using following documentation sites and repositories:

- https://protocol.docs.iex.ec/for-workers/manage-a-pool-of-workers
- https://github.com/iExecBlockchainComputing/deploy-workerpool

### Tutorial
1. Make sure you are in the "scheduler-core" directory
```bash
cd scheduler-core
```

2. Initialize iexec workspace
```bash
iexec init --skip-wallet
```

3. Check "chain.json" ( default has to be set to "bellecour")
```json
{
  "default": "bellecour",
  "chains": {
    "mainnet": {},
    "bellecour": {}
  }
}
```

4. Create iexec wallet (you will need to input a new password, e.g. "password123core")
```bash
iexec wallet create --keystoredir ./
```

5. Rename the newly created wallet (e.g. "core_wallet.json")

6. Localy initialize you workerpool registration
```bash
iexec workerpool init --wallet-file "core_wallet.json" --keystoredir ./
```

7. Edit the "iexec.json" and change the "workerpool.description". This field will appear publicly on the blockchain and the marketplace.

8. Make sure the "workerpool.owner" field of iexec.json file matches the "address" field of the "core_wallet.json" file.
```bash
jq .workerpool iexec.json
```

```bash
jq .address core_wallet.json
```

9. Register your workerpool on the blockchain to get its workerpool address
```bash
iexec workerpool deploy --wallet-file "core_wallet.json" --keystoredir ./
```

You may now check the workerpool metadata by typing your workerpool address into the search area on the explorer webpage (https://explorer.iex.ec/bellecour).

10. Register an ENS and setup both ENS resolution and reverse resolution to your workerpool's deployment address
```bash
ENS_WP_SUBDOMAIN="riteh-workerpool"
```

```bash
WP_ADDR="$(jq -r ".workerpool | first(.[])" deployed.json )"
```

```bash
iexec ens register "$ENS_WP_SUBDOMAIN" --for "$WP_ADDR" --wallet-file core_wallet.json --keystoredir ./
```

Check the workerpool settings (ENS name):
```bash
iexec workerpool show --raw | jq
```

11. [OPTIONAL] Set your workerpool's API URL. Set the PROD_CORE_HOST_DOMAIN

```bash
PROD_CORE_HOST_DOMAIN=core-prod.v8-bellecour.yourdomain
```

```bash
CORE_URL="https://$(grep 'PROD_CORE_HOST_DOMAIN=' .env | sed -e 's/PROD_CORE_HOST_DOMAIN=//')"
```

```bash
WP_ADDR="$(jq -r ".workerpool | first(.[])" deployed.json )"
```

```bash
iexec workerpool set-api-url "$CORE_URL" "$WP_ADDR" --wallet-file core_wallet.json --keystoredir ./
```

Check the workerpool settings (ENS name and API URL):
```bash
iexec workerpool show --raw | jq
```

12. Create a new Docker network (if the scheduler-core containers need to be on the same network as the worker containers)
```bash
docker network create iexec_network
```

13. Update the .env file to match your workerpool address and other parameters

14. Start the Docker containers.
```bash
docker compose up -d
```

15. Check the Grafana dashboard

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

### Task timeout
By default, maximum task compute time period is 300 seconds (5 minutes). If a Docker container (task) takes longer than that, the task will never finish and will hang until the task deadline (50 minutes). To change that, you have to set the workerpool task category. Default value is 0 (300) and the possible values are 0-5.

16. Set the category index to 2 (3600 seconds = 60 minutes) with 20 set as the volume (number of tasks that can be executed on this workerpool order - default value is 1). You can have multiple workerpoolorders (e.g. category 0 and category 1, etc.). Example:

```bash
iexec workerpool publish 0xb146c478acf118bE2Bd1524bb8E9A73ddbc20D40 --category 2 --volume 20 --wallet-file "core_wallet.json" --keystoredir ./
```