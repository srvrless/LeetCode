from collections import Counter

words = ["mass", "as", "hero", "superhero"]


def aaa():
    result = []
    for i in words:
        for x in words:
            if x in i:
                result.append(x)
    return [x[0] for x in Counter(result).items() if x[1] >= 2]


print(aaa())