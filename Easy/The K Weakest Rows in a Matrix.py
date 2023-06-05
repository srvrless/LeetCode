from collections import Counter
mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
print()
res=[]
for i in range(len(mat[0])-1):
    c=Counter(mat[0][i])
    c1=Counter(mat[0][i+1])
    if c.get(1) <c1.get(1):
        res.append(i)
print(res)