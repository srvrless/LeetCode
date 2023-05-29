import datetime


class Solution:

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        ds = f"{str(day)}/{str(month)}/{str(year)}"
        dt = datetime.datetime.strptime(ds, "%d/%m/%Y")
        return dt.strftime("%A")