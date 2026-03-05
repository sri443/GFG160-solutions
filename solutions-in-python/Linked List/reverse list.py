class Solution:
  
    def reverseList(self, head):
        curr = head
        prev = None
      
        while curr is not None:      #Traversing one by one
            nex = curr.next          #Storing the next of current node
            curr.next = prev         #Changing link of current node to point to previous node
            prev = curr              #Updating prev value to recently modified node (curr), then moving current pointer to next node (stored)
            curr = nex
          
        return prev       

#prev is now at the last node (of original list)
#All the links in the list now point backwards
#Hence prev becomes starting point of the new list
