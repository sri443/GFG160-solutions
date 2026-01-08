class Solution:
    def removeLoop(self, head):

      #No loop if empty list or only one node
        if head is None or head.next is None:
            return

        fast = head
        slow = head

        # Step 1: Detect the loop
        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                # Loop detected, break to find the start of the loop
                break

        # If a loop was detected (fast == slow)
        if fast == slow:
            # Step 2: Find the start of the loop
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next

            # Step 3: Find the last node in the loop and break the connection
            while fast.next != slow:
                fast = fast.next
            
            fast.next = None
