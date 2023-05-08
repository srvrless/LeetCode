import re
from typing import List
from collections import Counter


class Solution:

    def shortestCompletingWord(self, l: str, w: List[str]) -> str:
        pattern = r"[^a-zA-Z]"
        xd = re.sub(pattern, "", l.lower())
        xd_count = Counter(xd)
        w = sorted(w, key=len)
        return next((x for x in w if Counter(x) & xd_count == xd_count), None)