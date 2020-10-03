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
All variables and arguments used in this issue are single.

There is no loop processing and a constant number of spaces are used for adding blocks.

- BlockChain
  - __init__
    - $O(1)$.
  - add_chain
    - $O(1)$.
- Block
  - __init__
    - $O(1)$
  - calc_hash
    - $O(1)$

## About implementation
When adding a new block, it loops to the end and sets the hash value of the last block to the latest block.

Also, the seed value is set to fix the output.