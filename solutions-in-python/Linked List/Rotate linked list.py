class Solution:
    def rotate(self, head, k):
        
        if not head or not head.next:      #If empty or one node then nothing to rotate
            return head
        
        length = 1
        temp = head
        while temp.next:                 #Loop to count number nodes
            length +=1                   #And move to the last node (where we'll attach rotated part)
            temp = temp.next
            
        k = k % length                   #If number of rotations more than nodes then use remainder (circular)
        if k == 0:                       #If number of rotations is 0 then return list as it is
            return head
            
        curr = head
        for i in range(1,k):             #Loop to find the new list starter (where the list is cut-off)
            curr = curr.next
            
        new_head = curr.next             #Assigning new starter for the list based on rotation
        curr.next = None                 #Un-linking the current node (one before cut-off) from the list (new head)
        
        temp.next = head                 #Adding the un-linked part from the start of original list to the end of new list
        
        return new_head                  #Return the new head from where rotated list begins
