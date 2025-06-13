# Provider


## References
- https://docs.golem.network/docs/providers/provider-installation
- https://docs.golem.network/docs/providers/configuration/general

## Installing the provider
1. Launch your terminal and execute the following command to run the installer:

```bash
curl -sSf https://join.golem.network/as-provider | bash -
```

2. After installing all required components, you will be asked to set up your node, by providing configuration values. If you leave them empty, the default values (presented in brackets) will be applied. Press Enter for each entry to save it.

``Node name (default=generated-name)``

``Ethereum wallet address (default=internal wallet)``

``price GLM per hour (default=0.1)``

3. Add installation to system PATH. This step ensures that you can run Golem commands directly from the terminal without having to specify the full path to the executable each time.

For users utilizing the bash shell, you can modify your .bashrc file to update your PATH with the following command:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

Then, refresh your shell environment with the new PATH using:

```bash
source ~/.bashrc
```

4. Set the provider payment network to testnet
```bash
golemsp settings set --payment-network testnet
```

## Running the provider
5. To run the Golem provider on the testnet, type the following command into the terminal:
```bash
golemsp run --payment-network testnet
```

To check your node's status and see if it is active and computing tasks from the network, open a new terminal window and type:

```bash
golemsp status
```

6. Check provider status and settings

```bash
golemsp status
```

```bash
golemsp settings show
```