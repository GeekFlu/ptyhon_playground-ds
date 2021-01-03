# Block Chain

## Design
- To build the chain I have used linked a doubly linked list, the reason for this is for inserting in constant time, but given the distributed
  context of blockchain I do not know if this is helpful, but it is for this program
- The main Node (Block) of the linked list has the next attributes
    - timestamp
    - data
    - hash
    - previous_hash
    
- Every time we create a node all the attributes are hashed and assigned to hash property for getting the previous hash 
we assign it using the tail reference of the link list
## Time complexity
- Time complexity for add a block is in constant time O(1)
## Space Complexity
- The space complexity required is O(n) where n is a block with all the data
### Reference Links
- [Block Chain Rest API](https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/)
- [Blockchain Wiki](https://en.wikipedia.org/wiki/Blockchain)