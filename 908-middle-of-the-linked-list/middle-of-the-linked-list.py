class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        n=0
        temp=head 

        while temp is not None:
            n+=1
            temp=temp.next 

        temp=head 
        for i in range(0,n//2):
            temp=temp.next
        return temp       