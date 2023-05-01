from collections import Counter


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
xd = paragraph.replace(',', '').replace('.', '').lower().split()
x = Counter(xd)
del x[banned[0]]
print(x)
# print( max(x,key=x.get, default=None))