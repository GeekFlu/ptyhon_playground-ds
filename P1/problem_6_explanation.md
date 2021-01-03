# Union and Intersection of Two Linked Lists

## Design and time complexity
- These are the methods used in the solution
    - append - this method appends @ the end of the list in linear time O(n)
    - to_list - converts the nodes and return a list of the values, time complexity O(n), and we are using extra space O(2n)
    - search - search the value in the list in linear time O(n)
    - remove - removes an item in linear time O(n)
    - pop - removes the first element (head) in constant time O(1)
    - insert - inserts in linear time an element in given position O(n)
    - size - returns the size in constant time O(1)
    - get_unique_element_list - returns a list of unique elements (no duplicates) in linear time O(n)

## Time complexity
- union we are using a set to discard duplicates and then create a new union list in linear time O(n)
- intersection
    1. Will determine which list has the least elements
    2. Will iterate over this list and if the element is in the other list will add it to the dictionary
    3. Will create an intersection list based on the dictionary
    4. This method runs in linear time O(n)
## Space complexity
- The space complexity required for union is:
  - we are creating extra space for a set O(n) plus linked list O(n) = O(2n) = O(n)
- - The space complexity required for intersection is:
  - we are creating extra space for a dictionary O(m) plus linked list O(n) = O(m) + O(n) = O(m + n)
### Reference Links
- [Union, intersection reference](https://www.geeksforgeeks.org/union-intersection-two-linked-lists-set-3-hashing/)