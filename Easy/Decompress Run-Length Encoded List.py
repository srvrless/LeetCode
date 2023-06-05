nums = [1,2,3,4]

x=[]
for i,y in enumerate(nums):
    if i%2 != 0:
        continue
    x+=([nums[i+1]]*nums[i])
print(x)