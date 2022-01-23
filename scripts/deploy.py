from brownie import FundMe, accounts, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    deploy_mocks,
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    FORKED_LOCAK_ENVIRONMENTS,
)

##When we delete the ganche UI blockchain, we need to delete the 1337 deployments and from map.json


def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][
            network.show_active()
        ][  # This is forking
            "eth_usd_price_feed"
        ]
    else:  # This is mocking, where we create our own price feed contract
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    return fund_me

    print(f"Contract Deployed to {fund_me.address}")


def main():
    deploy_fund_me()
