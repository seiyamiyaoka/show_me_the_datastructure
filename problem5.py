import hashlib
import random

random.seed(1)

class BlockChain:
  def __init__(self, head):
    self.head = head
    self.tail = head

  def add_chain(self, new_block):
    if isinstance(self.head, Block):
      block = self.tail
      new_block.previous_hash = block.hash
      block.next = new_block
      self.tail = new_block
    else:
      print("No valid block is set")
      return

class Block:
  def __init__(self, timestamp, data, previous_hash=None):
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.calc_hash()
    self.next = None

  def calc_hash(self):
    sha = hashlib.sha256()
    sha.update(str(random.random() * 100).encode('utf-8'))

    return sha.hexdigest()

# case standard
chain = BlockChain(Block(12, 'hello', 0))

chain.add_chain(Block("", 'kojiro'))
chain.add_chain(Block(None, 'kojiro'))
chain.add_chain(Block(None, None))
chain.add_chain(Block("", ""))

block = chain.head
while block is not None:
  print("check: hash")
  print(block.hash)
  print("check: previous_hash")
  print(block.previous_hash)
  block = block.next
  # check: hash
  # 8f10e410fdef7119b03a3c302117e3732b5e8b40d7759b825ec19400be3f9a2f
  # check: previous_hash
  # 0
  # check: hash
  # 8ad0de39ca29445c885a6224add8f03ba0a0d28dba5c7f2f963b96fce4553947
  # check: previous_hash
  # 8f10e410fdef7119b03a3c302117e3732b5e8b40d7759b825ec19400be3f9a2f
  # check: hash
  # ddd22fb235dffc9cb3716c02c0e56d04acd27e0be5feef87ab0a406f42371f7b
  # check: previous_hash
  # 8ad0de39ca29445c885a6224add8f03ba0a0d28dba5c7f2f963b96fce4553947
  # check: hash
  # 99c5875334f709b0ecae8ca1ffdc7b2cc03d43665ac7ae2a21ade613a3ff66c4
  # check: previous_hash
  # ddd22fb235dffc9cb3716c02c0e56d04acd27e0be5feef87ab0a406f42371f7b
  # check: hash
  # bf25b109b4381e9041ac2ece0fa2b522a88c06ef8ea0434770cacf8ec98a220a
  # check: previous_hash
  # 99c5875334f709b0ecae8ca1ffdc7b2cc03d43665ac7ae2a21ade613a3ff66c4

# case head is None
chain = BlockChain(None)
chain.add_chain(Block("", 'kojiro'))
# No valid block is set

# case head is int
chain = BlockChain(1234)
chain.add_chain(Block("", 'kojiro'))
# No valid block is set

# case head is empty value
chain = BlockChain("")
chain.add_chain(Block("", 'kojiro'))
# No valid block is set