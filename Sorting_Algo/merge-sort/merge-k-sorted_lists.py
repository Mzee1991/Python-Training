# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        self.allNodes = []
        
        for l in lists:
            while l:
                self.allNodes.append(l.val)
                l = l.next
        self.allNodes.sort()
        
        current = point = ListNode(0)
        for i in self.allNodes:
            current.next = ListNode(i)
            current = current.next
        
        return point.next
