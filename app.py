import json
from web3 import Web3

# infura_url = "infura_url"
#
# web3 = Web3(Web3.HTTPProvider(infura_url))

ganache_url = "http://ganache_url"

web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = "xxxxxxxACCOUNT1xxxxxxxxxxxxxxxxxxxxxxxxxxx"
account_2 = "xxxxxxxACCOUNT2xxxxxxxxxxxxxxxxxxxxxxxxxxx"

private_key = "private_keyprivate_key"

nonce = web3.eth.getTransactionCount(account_1)

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei(50, 'gwei')
}

signed_tx = web3.eth.account.sign_transaction(tx, private_key)
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
