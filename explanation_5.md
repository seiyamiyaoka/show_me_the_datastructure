# Blockchain

## About data structure
- LinkedList
  - I chose LinkedList because I wanted to use data connections.

## About Order complexity
$O(1)$
Set "head" and "tail" in the BlockChain constructor.
The last block is stored by the block_chain object.

The Order complexity is $O(1)$ because tail can be accessed when adding a block.

## About Space complexity
Focusing on the add_chain method, the amount of space complexity is the amount of memory in self.tail.

self.tail is an instance of Block.
This space complexity is 64 bytes.

Focusing on the calc_hash method, the amount of space complexity is 40byte.

## About implementation
When adding a new block, it loops to the end and sets the hash value of the last block to the latest block.

Also, the seed value is set to fix the output.