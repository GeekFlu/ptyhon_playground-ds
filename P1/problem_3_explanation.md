# Huffman Coding / Decoding - Data Compression

## Design
- We built a priority queue using a Min Heap, so every time que pop out a value from the priority queue we will get the min value of all the set.
  We are using an array to manipulate the heap, so every insertion and deletion happens in order.
- For coding and decoding a tree is built based on a HuffmanNode which contains frequency and character

## Time complexity
- Min heap time complexity for method poll happens in O(long n) since we have to keep the heap in the tree
  When we remove the root of the tree we swap the last value into the root, now we have to go down swapping values
  until the values are in place as expected.
- Min heap time complexity for method insert happens in O(long n) since we have to keep the heap in the tree, 
  since we start @ the leaf level of the tree we have to swap values with the parent until the values are placed as expected the lesser
  in the parent or even @ the root of tree.
- Min heap time complexity for method peek is O(1) we only return the first value of the array
- Min heap time complexity for method size is O(1) we return the elements in the array

- For huffman_encoding we are expecting a time complexity of O(n Log n), since we are processing n nodes, but we are using poll and insert Min Heap's methods until our priority
  queue is empty O(n * log n)
- For huffman_decoding we are expecting a time complexity of O(n Log n), since we are processing n nodes, and traversing a tree in log n time
  
### Reference Links
- [Huffman and tress explanation](http://homepages.math.uic.edu/~jan/mcs360/heaps_and_trees.pdf)
- [Heap - Heap Sort - Heapify - Priority Queues](https://www.youtube.com/watch?v=HqPJF2L5h9U)
- [Heaps](https://www.youtube.com/watch?v=t0Cq6tVNRBA)