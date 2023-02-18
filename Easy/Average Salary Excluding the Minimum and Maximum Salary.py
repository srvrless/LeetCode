class Solution:
    def average(self, salary: List[int]) -> float:
        m = max(salary)
        m1 = min(salary)
        salary.remove(m)
        salary.remove(m1)
        return sum(salary) / len(salary)
