class Solution:

    def dayOfYear(self, dat: str) -> int:
        year, month, day = map(int, dat.split('-'))
        timedelta = date(year, month, day) - date(year - 1, 12, 31)
        return timedelta.days