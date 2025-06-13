# Ganache tutorial
This is a work-in-progress tutorial for starting a private Ganache test blockchain, deploying iExec PoCo smart contracts on it and using it to register an iExec workerpool.

## Ganache blockchain
1. Start Ganache AppImage (GUI app)

You can download the image from https://archive.trufflesuite.com/ganache/

2. Set up a workspace by going to the SERVER tab in the options and set these values
```
Hostname = 0.0.0.0 - All Interfaces
```
```
Port number = 8545
```
```
Network ID = 1337
```

3. Start the workspace

Ganache starts the blockchain with 20 preset accounts. Every account has an address and a private key.

## Deploy iExec PoCo smart contracts

4. Clone GitHub repo (https://github.com/iExecBlockchainComputing/PoCo)

```bash
git clone https://github.com/iExecBlockchainComputing/PoCo.git
```

```bash
cd PoCo
```

5. Edit ``config/config.json``. Add your chain by using its ID (1337).

```json
"1337": {
    "_comment": "asset should be Token or Native",
    "asset": "Native",
    "v3": {
        "Hub": null,
        "AppRegistry": null,
        "DatasetRegistry": null,
        "WorkerpoolRegistry": null
    },
    "v5": {
        "usefactory": true,
        "salt": "0x0000000000000000000000000000000000000000000000000000000000000000"
    }
},
```

6. Edit ``hardhat.config.json``. Add your network ("local").

```ts
local: {
  chainId: 1337,
  url: 'http://127.0.0.1:8545',
  accounts: [
    "0x8fb1f2fe84676c4b46ae6dc5613cff26d6ae25a92ef9f3c3ecb4a6e61b80c637",
    "0x0934a7bdec917c38baf0aec35eec9d84874a1912c529727b821da52f0439476b",
    "0x31e19c19f300ff734831eba61282cbe7062f1580f762c9cf6a6f395dcdd7b616",
    "0xb31a1121f4855e0cd32a1633f556174bd8326d47c36eb0b6a866bdf894b7cf50"
  ],
},
```

Set the chain ID and set URL to the Ganache RPC endpoint. For the accounts use one or more accounts set by the Ganache blockchain. You have to use private key for the account address.

7. Build and compile the Hardhat Node project.

```bash
npm install
```

```bash
npx hardhat compile
```

8. Deploy PoCo smart contracts to the Ganache blockchain.

```bash
npx hardhat deploy --network <your network name>
```

```bash
npx hardhat deploy --network local
```

9. Save the Chain Hub address. You can find it in the deployment logs or the output console:

```
ERC1538Proxy: 0xFBFa97176C6bbDa07aCB9554A01167Eb0bcECB65
```

## Setup iExec scheduler-core

10. Initialize the iExec workspace.

```bash
iexec init --skip-wallet
```

11. Edit the ``chain.json`` file. Use the generated chain hub address (ERC1538Proxy).

```json
{
  "default": "local",
  "chains": {
    "mainnet": {},
    "bellecour": {},
    "local": {
      "host": "http://localhost:8545",
      "iexecGateway": "http://localhost:3001",
      "id": "1337",
      "hub": "0xFBFa97176C6bbDa07aCB9554A01167Eb0bcECB65"
    }
  }
}
```

12. Import the wallet from one of your Ganache accounts.

```bash
iexec wallet import 0xb31a1121f4855e0cd32a1633f556174bd8326d47c36eb0b6a866bdf894b7cf50 --keystoredir ./
```

13. Rename it to "core_wallet.json".


14. Follow the ``scheduler-core`` instructions but add ``--chain local`` to ``workerpool deploy`` command.
```bash
iexec workerpool init --wallet-file "core_wallet.json" --keystoredir ./
```

15. Deploy the workerpool and save the generated workerpool address.
```bash
iexec workerpool deploy --wallet-file "core_wallet.json" --keystoredir ./ --chain local
```

# TODO