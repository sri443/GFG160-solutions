class Solution:
    def addTwoLists(self, head1, head2):
        def reverse(head):
            curr=head
            prev=None
            while curr:
                nextNode=curr.next
                curr.next=prev
                prev=curr
                curr=nextNode
            return prev
        
        head1=reverse(head1)
        head2=reverse(head2)
        
        dummy=Node(0)
        curr=dummy
        carry=0
        
        while head1 is not None or head2 is not None or carry!=0:
            val1=head1.data if head1 is not None else 0
            val2=head2.data if head2 is not None else 0
            total=val1+val2+carry
            carry=total//10
            
            curr.next=Node(total%10)
            curr=curr.next
            
            if head1:
                head1=head1.next
            if head2:
                head2=head2.next
                
        result=reverse(dummy.next)
        
        if not result:
            return Node(0)
        while result and result.data==0 and result.next:
            result=result.next
            
            
        return result
