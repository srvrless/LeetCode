class Solution:

    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in operations:
            if i.isdigit() or "-" in i:
                res.append(int(i))
            if i == 'C':
                res.pop()
            if i == 'D':
                res.append(res[-1] * 2)
            if i == '+':
                res.append(res[-2] + res[-1])
        return sum(res)