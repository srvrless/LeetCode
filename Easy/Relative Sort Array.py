arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
res = []
for i in range(len(arr2)):
    x = [arr2[i]] * arr1.count(arr2[i])
    res.extend(x)
    print(res)

