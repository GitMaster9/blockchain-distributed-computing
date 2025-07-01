# iExec Requester tutorial
This is a tutorial on how to use a Docker image for task execution as a requestor on the iExec Bellecour sidechain (testnet).
You can use any public Docker image or build your own.

### References
This repository was set up using following documentation sites and repositories:
- https://tools.docs.iex.ec/overview/helloWorld/3-buildIApp


### Tutorial
1. Initialize iexec workspace
```bash
iexec init --skip-wallet
```

2. Check "chain.json" ( default has to be set to "bellecour")
```json
{
  "default": "bellecour",
  "chains": {
    "mainnet": {},
    "bellecour": {}
  }
}
```

3. Create iexec wallet (you will need to input a new password, e.g. "password123requester")
```bash
iexec wallet create --keystoredir ./
```

4. Rename the newly created wallet (e.g. "requester_wallet.json")

5. Initialize iexec decentralized application (dApp, iApp)
```bash
iexec app init --wallet-file "requester_wallet.json" --keystoredir ./
```

This will generate the "app" part of the iexec.json config file. Edit that to your needs ("name" and Docker image - "multiaddr")

6. Deploy the application
```bash
iexec app deploy --wallet-file "requester_wallet.json" --keystoredir ./
```
This will generate the deployed.json file with the app address. You will use that address for publishing and running the app on the iExec network.

7. Publish the app
```bash
iexec app publish [appAddress] --wallet-file [walletName] --keystoredir ./
```

```bash
iexec app publish 0x06c35255c455d56f97D481666263069cf064eE22 --wallet-file "requester_wallet.json" --keystoredir ./
```

You can check the published apporders

```bash
iexec orderbook app [appAddress]
```

```bash
iexec orderbook app 0x06c35255c455d56f97D481666263069cf064eE22
```

8. Run the app on the specified workerpool you created with no parameters (default values will be used):
```bash
iexec app run [appAddress] --workerpool [workerpoolAddress] --wallet-file [walletName] --keystoredir ./
```

```bash
iexec app run 0x06c35255c455d56f97D481666263069cf064eE22 --workerpool 0x767eb830fd670d221C761b0c144a33Ec39a5902E --wallet-file "requester_wallet.json" --keystoredir ./
```

You can use a string argument to use for task output.

```bash
iexec app run [appAddress] --workerpool [workerpoolAddress] --wallet-file [walletName] --keystoredir ./ --args [StringArgument]
```

```bash
iexec app run 0x06c35255c455d56f97D481666263069cf064eE22 --workerpool 0x767eb830fd670d221C761b0c144a33Ec39a5902E --wallet-file "requester_wallet.json" --keystoredir ./ --args MyArgument
```

You can send simulation parameters to the Python script. Example:
```bash
iexec app run 0x06c35255c455d56f97D481666263069cf064eE22 --wallet-file "requester_wallet.json" --keystoredir ./ --args "--num_photons 1_000_000 --skip_full_result_save true"
```

This will create a deal with a generated ID (dealid).

9. Check the deal using the generated ID
```bash
iexec deal show [dealID]
```

```bash
iexec deal show 0x7289902470ab0936630c44b578f36e7746422b7913f7758ba4cffcb01d0b505b
```

This will output the task ID.

10. Check the task status
```bash
iexec task show [taskID]
```

```bash
iexec task show 0xf887f21cb2b387f72c9cc3fc0871e8ea902383cc9ac2dc708ab4b9fdfba76295
```

You can download the task output files with your wallet

```bash
iexec task show [taskID] --wallet-file [walletName] --keystoredir ./ --download
```

```bash
iexec task show 0xf887f21cb2b387f72c9cc3fc0871e8ea902383cc9ac2dc708ab4b9fdfba76295 --wallet-file "requester_wallet.json" --keystoredir ./ --download
```
