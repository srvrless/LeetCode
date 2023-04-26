class SmallestInfiniteSet:

    def __init__(self):
        self.a = list(range(1, 1001))

    def popSmallest(self) -> int:
        xself = self.a.index(min(self.a))
        return self.a.pop(xself)

    def addBack(self, num: int) -> None:
        if num not in self.a:
            self.a.append(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)