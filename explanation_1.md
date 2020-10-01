# Least Recently Used Cache

## About data structure
I used the HashMap data structure to hold the cache.

This is because the amount of calculation when registering a new cache and when retrieving data from the cache can be executed with 1.

## About Order complexity
$O(1)$

## About implementation

The big feature is to consider the order while using hashmap.

So I am re-registering the target cache if the cache hits when executing set and get.

With this feature I defined the data at the beginning of the cache as the least used data.

