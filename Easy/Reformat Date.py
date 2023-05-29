class Solution:
    def reformatDate(self, date: str) -> str:
       return datetime.datetime.strptime(re.sub(r"(st|th|rd|nd)", "", date), "%d %b %Y").strftime("%Y-%m-%d")



