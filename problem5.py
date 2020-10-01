import hashlib
import random

random.seed(1)

class BlockChain:
  def __init__(self, head):
    self.head = head
  def add_chain(self, new_block):
    block = self.head

    while block.next is not None:
      block = block.next
    new_block.previous_hash = block.hash
    block.next = new_block

class Block:
  def __init__(self, timestamp, data, previous_hash):
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.calc_hash()
    self.next = None

  def calc_hash(self):
    sha = hashlib.sha256()
    sha.update(str(random.random() * 100).encode('utf-8'))

    return sha.hexdigest()

chain = BlockChain(Block(12, 'hello', 0))
chain.add_chain(Block(12, 'kojiro', chain.head.hash))
chain.add_chain(Block(None, 'kojiro', chain.head.hash))


block = chain.head
while block is not None:
  print(block.hash)
  # first: 8f10e410fdef7119b03a3c302117e3732b5e8b40d7759b825ec19400be3f9a2f
  # second: 8ad0de39ca29445c885a6224add8f03ba0a0d28dba5c7f2f963b96fce4553947
  # third: ddd22fb235dffc9cb3716c02c0e56d04acd27e0be5feef87ab0a406f42371f7b
  block = block.next

