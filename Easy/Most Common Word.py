def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    pattern = r"[^\w\s]"
    xd = re.sub(pattern, "", paragraph.lower().replace(',',', '))
    xd=xd.split()
    x=Counter(xd)
    for i in range(len(banned)):
        del x[banned[i]]
    return max(x,key=x.get, default=None)