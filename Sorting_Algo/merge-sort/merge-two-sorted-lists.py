def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        current = list3
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = ListNode(list1.val)
                list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                list2 = list2.next
            current = current.next
        
        while list1:
            current.next = ListNode(list1.val)
            current = current.next 
            list1 = list1.next
        while list2:
            current.next = ListNode(list2.val)
            current = current.next
            list2 = list2.next
            
        return list3.next
