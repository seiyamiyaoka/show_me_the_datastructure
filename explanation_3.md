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

- huffman_encoding
  - $O(n)$. This is because when creating a heap, data is retained for the number of hash elements.
- create_binary
  - $O(n^2)$. This is because a result variable is prepared for each recursive process.
- huffman_decoding
  - $O(1)$. It is a constant because it is reassigned when searching the tree."decoded_data" is considered as a string.

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