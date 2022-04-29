from brownie import accounts
from scripts.get_weth import get_weth

# Forked chain
# we are going to point to a real chain, and make txs
# as if it was the main chain but local chain is running

def main():
    # deposit Money
    # The account that is going to call the function
    account = accounts[0]
    # WETH is wrapped ether
    # Weth allows us to use ETH as if it were an ERC20 token
    erc20_address = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
    # Approve the WETH token to be deposited to Aave
    get_weth(account)
    # ABI + address to call a function

def approve_erc20(amount, lending_pool_address, erc20_address):
    # ABI + address
    lending_pool = interface.LendingPoolInterface(lending_pool_address)
    # Approve the WETH token to be deposited to Aave
    tx = lending_pool.approve(erc20_address, amount, {"from": account})
    tx.wait(1)
    print("Approved {} WETH".format(amount))