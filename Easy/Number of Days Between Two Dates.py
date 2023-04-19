from datetime import datetime


class Solution:

    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = datetime.strptime(date1.replace('-', '/'), '%Y/%m/%d')
        date2 = datetime.strptime(date2.replace('-', '/'), '%Y/%m/%d')

        difference = date1 - date2
        duration_in_s = difference.total_seconds()
        return abs(int(divmod(duration_in_s, 86400)[0]))