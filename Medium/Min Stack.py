class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = 2**31 - 1

    def push(self, val: int) -> None:
        if val <= self.minVal:
            self.stack.append(self.minVal)
            self.minVal = val
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.minVal:
            self.minVal = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal