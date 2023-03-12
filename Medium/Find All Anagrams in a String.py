# Not working
def asynchron():
    res=[]
    xss=len(p)
    for i,y in enumerate(s):
        x=(s[i:i+xss])
        if sorted(x) == sorted(p):
            res.append(i)
    return res
print(asynchron())