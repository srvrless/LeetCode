from collections import Counter

name = "saeed"
typed = "ssaaedd"
s1 = Counter(name)
s2 = Counter(typed)
for i in name:
    if s1.get(i) < s2.get(i):
        print(False)
        break
