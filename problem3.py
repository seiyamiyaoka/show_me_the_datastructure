import sys
import heapq
import random
random.seed(1)

class Node:
  def __init__(self, value, frequency):
    self.value = value
    self.frequency = frequency
    self.left = None
    self.right = None

def huffman_encoding(data):
  hash = {}
  memo = {}
  encode_data = ""
  priority_queue = []

  is_valid = len(data) > 0

  assert is_valid, 'please input any char'

  for char in data:
    hash[char] = hash.get(char, 0) + 1

  for index, item in enumerate(hash.items()):
    heapq.heappush(priority_queue, tuple((item[1], index, Node(item[0], item[1]))))

  if len(priority_queue) > 1:
    while len(priority_queue) > 1:
      left = heapq.heappop(priority_queue)
      right = heapq.heappop(priority_queue)

      merge_node = Node("", "")
      merge_node.left = left[2]
      merge_node.right = right[2]

      heapq.heappush(priority_queue, tuple((left[0] + right[0], left[0] + int(random.random() * 1000), merge_node)))

  for char in data:
    if char in memo:
      encode_data += memo[char]
    else:
      result = create_binary(priority_queue[0][2], char, "")
      encode_data += result
      memo[char] = result

  return encode_data, priority_queue

def create_binary(tree, target_char, binary_str):
  result = ""
  if tree.value == target_char:
    if len(binary_str) > 0:
      return binary_str
    else:
      return "0"
  if tree is not None:
    if tree.left is not None:
      result = create_binary(tree.left, target_char, binary_str + "0")
      if result:
        return result
    if tree.right is not None:
      result = create_binary(tree.right, target_char, binary_str + "1")
      if result:
        return result
  return result

def huffman_decoding(data, tree):
  decode_data = ""
  head = tree
  depth_is_one = tree.left is None and tree.right is None

  while data:
    if tree and tree.left is None and tree.right is None:
      decode_data += tree.value
      tree = head
    if tree:
      if tree.left is not None and int(data[0]) == 0:
        tree = tree.left
      elif tree.right is not None and int(data[0]) == 1:
        tree = tree.right
    data = data[1:]
  if depth_is_one is False:
    decode_data += tree.value
  return decode_data

if __name__ == "__main__":
    codes = {}

    # test case 1
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 69
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is: The bird is the word
    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 36
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 1000010011110100111110000011101111111001101110101001111010101011000001
    decoded_data = huffman_decoding(encoded_data, tree[0][2])

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 69
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: The bird is the word

    # # # test case 2

    a_great_sentence = "こんにちは"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 84
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is: こんにちは
    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 28
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 110111000110
    decoded_data = huffman_decoding(encoded_data, tree[0][2])

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 84
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: こんにちは

    # test case 3 repeat value

    a_great_sentence = "AAAAAAAAAA"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 84
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is: こんにちは
    encoded_data, tree = huffman_encoding(a_great_sentence)
    # import pdb; pdb.set_trace()

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 28
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 110111000110
    decoded_data = huffman_decoding(encoded_data, tree[0][2])

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 84
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: こんにちは

    # # # test case 4 empty value
    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 49
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is:
    encoded_data, tree = huffman_encoding(a_great_sentence)
    # Traceback (most recent call last):
    # File "problem3.py", line 129, in <module>
    # encoded_data, tree = huffman_encoding(a_great_sentence)
    # File "problem3.py", line 20, in huffman_encoding
    # assert is_valid, 'please input any char'
    # AssertionError: please input any char
