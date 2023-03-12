class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        count = 0
        result = None
        current = self.head
        while current:
            count += 1
            # Select the current node with probability 1/count
            if random.randint(1, count) == 1:
                result = current.val
            current = current.next
          
        return result