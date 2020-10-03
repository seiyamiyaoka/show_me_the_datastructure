class LRU_Cache(object):
  def __init__(self, capacity):
    self.capacity = self._is_valid_capacity(capacity)
    self.cache = {}

  def get(self, key):
    if key in self.cache:
      tmp_value = self.cache[key]
      del self.cache[key]
      self.cache[key] = tmp_value
      return self.cache[key]
    else:
      return -1

  def set(self, key, value):
    if key == None:
      print("You can't set None!!")
      return
    if key in self.cache:
      del self.cache[key]
    else:
      if self.capacity is not None:
        if self.capacity <= 0:
          del self.cache[list(self.cache.keys())[0]]
        self.capacity -= 1
        self.cache[key] = value

  def _is_valid_capacity(self, capacity):
    if capacity is None or capacity <= 0:
      print("Please add a positive integer")
      return None
    else:
      return capacity

# case 1 max capacity 5
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(None, 1)
# display "You can't set None!!"
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)

print(our_cache.cache)

print(our_cache.get(1))
# returns 1
print(our_cache.get(2))
# returns 2
print(our_cache.get(9))
# returns -1
print(our_cache.get(""))
# returns -1
print(our_cache.get(None))
# returns -1
our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache.get(3))
# returns -1

## case 2 max capacity negative number
our_cache = LRU_Cache(-1)
# print Please add a positive integer
our_cache.set(1, 1)
our_cache.set(None, 1)
# print "You can't set None!!"
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)

## case 3 capacity is None
our_cache = LRU_Cache(None)
# print Please add a positive integer
our_cache.set(1, 1)
our_cache.set(None, 1)
# print "You can't set None!!"
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)

## case 4 large capacity(1000)

our_cache = LRU_Cache(1000)

for i in range(1000):
  our_cache.set(i, i)

print(our_cache.get(0))
# 0
our_cache.set(1000, 1000)
import pdb; pdb.set_trace()
print(our_cache.get(1))
# -1
