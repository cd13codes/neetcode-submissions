# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=fast=head
        counter=0
        prev=None
        


        while fast and fast.next :
            slow=slow.next
            fast=fast.next.next
       
        while slow!=None:
            newnode=slow.next
            slow.next=prev
            prev=slow
            slow=newnode
        f,s=head,prev

        while s.next!=None:
            t1,t2=f.next,s.next
            f.next=s
            s.next=t1
            f,s=t1,t2
        


            
            




            

        
        