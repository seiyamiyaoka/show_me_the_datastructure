# Least Recently Used Cache

## About data structure
I used the HashMap data structure to hold the cache.

This is because the amount of calculation when registering a new cache and when retrieving data from the cache can be executed with 1.

## About Order complexity
$O(1)$
The "get" and "set" methods access the cache.

The Order complexity is $O(1)$ because the data can be specified at once by the key.

## About Space complexity
- __init__(self, capacity)
  - $O(1)$. This is because one value is set for self.capacity and self.cache. => $O(2)$ => $O(1)$
- get(self, key):
  - $O(n)$. The key received as an argument requires a capacity of 1. The self.cache will increase by the size of capacity at the maximum. therefor capacity is n. => $O(n + 1)$ => $O(n)$
- set(self, key, value)
  - $O(n)$. It's almost the same as get method.
- _is_valid_capacity(self, capacity)
  - $O(1)$
## About implementation

The big feature is to consider the order while using hashmap.

So I am re-registering the target cache if the cache hits when executing set and get.

With this feature I defined the data at the beginning of the cache as the least used data.

