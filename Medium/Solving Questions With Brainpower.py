q = [[21, 5], [92, 3], [74, 2], [39, 4], [58, 2], [5, 5], [49, 4], [65, 3]]
solve_offset = 6
result = 0
for i in range(len(q)):
    ans = []
    ans.append(q[i][0])
    if len(q[i + solve_offset:]) >= 1:
        ans.append(q[i + solve_offset:][0][0])
    if sum(ans) > result:
        result = sum(ans)
    print(ans)
print(result)