class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None: return l2
        elif l2 is None: return l1
        head = ListNode(None)
        tail = head
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else: # l2.val < l1.val
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 is not None else l2

        return head.next
        #Extra Memory: O(1)
        #Runtime O(l1+l2)
