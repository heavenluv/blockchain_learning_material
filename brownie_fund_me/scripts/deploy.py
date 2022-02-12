from brownie import FundMe
from scripts.helpful_scirpts import get_account

def deploy():
    account = get_account()
    fund_me = FundMe.deploy({"from": account}, publish_source=True)
    print(f"Contract deployed to {fund_me.address}")

def main():
    deploy()