arr = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
n = 2
res = []

for i in range(n):
    if len(res) >0:
        arr=res
        res=[]
    for x in arr:
        if type(x) == list:
            for a in x:
                res.append(a)
        else:
            res.append(x)
print(res)