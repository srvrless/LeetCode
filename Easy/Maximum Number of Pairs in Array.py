class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs = 0
        left = 0
        for num, cnt in Counter(nums).items():
            pairs += cnt >> 1
            left += cnt & 1
        return pairs, left