# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l = 0
        temp = head
        while temp:
            temp = temp.next
            l += 1
        temp = head
        for _ in range(l//2-1):
            temp = temp.next
            
        if(temp.next):
            temp.next = temp.next.next
        else:
            head = head.next
        
        return head
        