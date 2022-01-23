from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3

FORKED_LOCAK_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
DECIMALS = 8
START_PRICE = 200000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAK_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"Active network is {network.show_active()}")
    print("Deploying mocks...")
    if len(MockV3Aggregator) < 1:
        MockV3Aggregator.deploy(DECIMALS, START_PRICE, {"from": get_account()})
    print("Mocks Deployed")
