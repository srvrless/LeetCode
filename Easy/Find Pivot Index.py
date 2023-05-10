nums = [1,7,3,6,5,6]
for i in range(len(nums)-1):
    s1 = nums[i+1:]
    s2 = nums[:i-1]
    print(s1,s2)
    # if sum(s1[1:])==sum(s2):
