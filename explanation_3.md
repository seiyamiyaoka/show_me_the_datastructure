# Huffman Coding

## About data structure

- hashmap
  - I'm using a hashmap data structure to hold of how often characters appear.
  - I am using it as a memo to identify the binary to encode.This is to reduce the time to traverse.
- heap(min)
  - I'm using it to rebuild the Tree as in the hint

## About Order complexity

- huffman_encoding
  - $O(n log n)$: Create a binary tree when you create a heap data structure in python. It requires $O(nlogn)$ complexity to execute it n times.
- huffman_decoding
  - $O(n log n)$

## About Space complexity

### encode
Computational complexity $O(n log n)$ is required to create a binary tree.
$O(n log n)$ Nodes are created.

Calculates the data type assigned to the local variable used when encoding.

node_instance_size = 64 => Node instance size
hash = 248 => default dict size
memo = 248 => default dict size
encode_data = 49 => string
priority_queue = 72 => empty list size
is_valid = 28 => bool size(24(False) or 28(True))
merge_node = 64 => Node instance size
left = 72 => heap list size
right = 72 => heap list size
result = 48 => string

((n log n) * node_instance_size) + hash + memo + encode_data + priority_queue + is_valid + merge_node + left + right + result

### decode

decode_data = 48 => string
head = 72 => heap list
tree = 72 => heap list
data = 48 => string

n = Number of reached leaf

The number of bytes of the leaf value string is added when decoding.
The amount of data when added is 1 byte.

decode_data + n + head + tree + data

## About implementation

```py
heapq.heappush(priority_queue, tuple((left[0] + right[0], left[0] + int(random.random() * 1000), merge_node)))
```
I use large random numbers when using data for heap because Node objects are incomparable objects.

When creating binary data, it has a data structure ordered by heap, so you can easily create data by adding 0 or 1 at the end each time you search.

Even when decoding, the tree information is retained, so you can restore the data by searching from the beginning until you reach the leaf.