class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        remove_count = int(len(arr) * 0.05)
        arr = arr[remove_count:-remove_count]
        return sum(arr) / len(arr)
