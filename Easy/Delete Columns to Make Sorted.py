strs = ["cba", "daf", "ghi"]

for i in range(len(strs[0])):
    q = ''
    for x in range(len(strs[0])):
        q += strs[x][i]
    if q != ''.join(sorted(q)):
        print(sorted(q))
        # return x