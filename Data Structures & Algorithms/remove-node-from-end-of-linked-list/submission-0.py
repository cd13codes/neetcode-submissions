# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr1=ptr=head
        k=1
    
        while ptr.next != None :
            ptr=ptr.next
            k=k+1
        # print(k)

        if n==k:
            return head.next

        else:

            for i in range(0,k-n-1):
                ptr1=ptr1.next
            ptr1.next=ptr1.next.next

            return head
            


        