list1 = ["happy", "sad", "good"]
list2 = ["sad", "happy", "good"]


def findRestaurant():
    common = set(list1) & set(list2)
    print(common)
    min_sum = float('inf')
    result = []
    for restaurant in common:
        curr_sum = list1.index(restaurant) + list2.index(restaurant)
        if curr_sum < min_sum:
            min_sum = curr_sum
            result = [restaurant]
        elif curr_sum == min_sum:
            result.append(restaurant)
    return result


print(findRestaurant())