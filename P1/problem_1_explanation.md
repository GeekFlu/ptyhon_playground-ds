# Least Recently Used Cache

## Design

1. I am using a Queue which is implemented using a doubly linked list. 
2. The maximum size of the queue will be equal to the total number of frames available (cache size). 
   The most recently used pages will be near front end and least recently pages will be near the rear end.
3. We are using a dictionary to keep track of the active nodes (valid) that the cache has.
      
## Time complexity
All operations are executed in constant time O(1)
- We are using front reference to insert at the beginning
- I case of a hit we get the reference node the dictionary and push it again to the front of the queue
- If some element is discarded because is out of we are using the rear reference to remove it from the list

## Reference Links
- [LRU Implementation](https://www.geeksforgeeks.org/lru-cache-implementation/)