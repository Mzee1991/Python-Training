# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        sortedLis=[]
        tmp=head
        while tmp:
            sortedLis.append(tmp.val)
            tmp=tmp.next
        sortedLis.sort()
        tmp=head
        for x in sortedLis:
            tmp.val=x
            tmp=tmp.next
        return head
