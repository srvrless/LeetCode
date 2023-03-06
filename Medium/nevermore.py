def dailyTemperatures(temp):
    res = []
    sss = len(temp)
    try:
        for i, y in enumerate(temp):
            count=1
            if temp[i] > temp[i + 1]:
                for x in range(i+1, sss):

                    if temp[i] > temp[x]:
                        count += 1
                    if temp[i] < temp[x]:
                        res.append(count)
                        break
            if temp[i] < temp[i + 1]:
                res.append(1)

        return res
    except Exception as e:
        return res, e


print(dailyTemperatures(temp=[73, 74, 75, 71, 69, 72, 76, 73]))
