class Solution:

    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) == 1 or len(arr) == 2:
            return False
        c = arr.index(max(arr))
        if c == len(arr) - 1 or c == 0:
            return False
        print(c)
        for i in range(c - 1):
            if arr[i] >= arr[i + 1]:
                return False
        for i in range(c, len(arr) - 1):
            if arr[i] <= arr[i + 1]:
                return False
        return True