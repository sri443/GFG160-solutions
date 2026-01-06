"""
class Node:
    def __init__(self, data):   
        self.data = data
        self.next = None
"""

class Solution:
    def cycleStart(self, head):
        if head is None or head.next is None:
            return -1
        fast=head
        slow=head
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                break
        else:
            return -1
            
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow.data
