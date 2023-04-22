def diStringMatch(self, S: str) -> List[int]:
    s, l = 0, len(S)
    res = []
    for c in S:
        if c == "I":
            res.append(s)
            s += 1
        else:
            res.append(l)
            l -= 1
    res.append(s)
    return res
