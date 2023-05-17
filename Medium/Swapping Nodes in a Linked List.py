class Solution:
    def swapNodes(self, head, k):
        
        number  =  head
        for _ in range(k-1):
            number  =  number.next
        
        a  =  number
        b  =  head
        
        while number.next:
            b  =  b.next
            number  =  number.next
        
        a.val, b.val  =  b.val, a.val
        
        return head