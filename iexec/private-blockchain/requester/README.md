# Requester tutorial

1. Make sure you are in the "requester" directory
```bash
cd requester
```

2. Initialize iexec workspace
```bash
iexec init --skip-wallet
```

4. Import iexec wallet (you will need to input a new password, e.g. "password123requester")
```bash
iexec wallet import 0xb31a1121f4855e0cd32a1633f556174bd8326d47c36eb0b6a866bdf894b7cf50 --keystoredir ./
```

5. Rename the newly created wallet (e.g. "requester_wallet.json")

6. Initialize iexec decentralized application (dApp, iApp)
```bash
iexec app init --wallet-file "requester_wallet.json" --keystoredir ./
```

This will generate the "app" part of the iexec.json config file. Edit that to your needs ("name" and Docker image - "multiaddr")

7. Deploy the application
```bash
iexec app deploy --wallet-file "requester_wallet.json" --keystoredir ./ --chain local
```
This will generate the deployed.json file with the app address. You will use that address for publishing and running the app on the iExec network.

8. Publish the app
```bash
iexec app publish [appAddress] --wallet-file [walletName] --keystoredir ./
```

```bash
iexec app publish 0xB498a789aDC8a40d6d0882B167AF0C889A80505f --wallet-file "requester_wallet.json" --keystoredir ./ --chain local
```

You can check the published apporders

```bash
iexec orderbook app [appAddress]
```

```bash
iexec orderbook app 0xB498a789aDC8a40d6d0882B167AF0C889A80505f
```

9. Run the app on the specified workerpool you created
```bash
iexec app run [appAddress] --workerpool [workerpoolAddress]
```

```bash
iexec app run 0xB498a789aDC8a40d6d0882B167AF0C889A80505f --workerpool 0x41beB7Bffa4284e2b647C180581Ad3dC2F023898 --wallet-file "requester_wallet.json" --keystoredir ./
```

You can use a string argument to use for task output.

```bash
iexec app run [appAddress] --workerpool 0x41beB7Bffa4284e2b647C180581Ad3dC2F023898 --args [StringArgument]
```

```bash
iexec app run 0xB498a789aDC8a40d6d0882B167AF0C889A80505f --workerpool 0x41beB7Bffa4284e2b647C180581Ad3dC2F023898 --args MyArgument
```

This will create a deal with a generated ID (dealid).

10. Check the deal using the generated ID
```bash
iexec deal show [dealID]
```

```bash
iexec deal show 0x7289902470ab0936630c44b578f36e7746422b7913f7758ba4cffcb01d0b505b
```

This will output the task ID.

11. Check the task status
```bash
iexec task show [taskID]
```

```bash
iexec task show 0xf887f21cb2b387f72c9cc3fc0871e8ea902383cc9ac2dc708ab4b9fdfba76295
```

You can download the task output

```bash
iexec task show [taskID] --download
```

```bash
iexec task show 0xf887f21cb2b387f72c9cc3fc0871e8ea902383cc9ac2dc708ab4b9fdfba76295 --download
```