from block import Block

blockchain = []

genesis_block = Block("Here we go...", ["Jack sent 5 BTC to Mike"])

second_block = Block(genesis_block.block_hash, ["Mike sent 10 BTC to Jack"])

third_block = Block(second_block.block_hash, ["Jack sent 5 BTC to Mike"])

print("Block hash: genesis block:")
print(genesis_block.block_hash)

print("Block hash: second block:")
print(second_block.block_hash)

print("Block hash: third block:")
print(third_block.block_hash)

