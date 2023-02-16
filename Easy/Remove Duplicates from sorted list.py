class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        pt = head
        prev = pt
        pt = pt.next
        while pt:
            if pt.val == prev.val:
                prev.next = pt.next
                pt = pt.next
            else:
                prev = pt
                pt = pt.next
        return head
