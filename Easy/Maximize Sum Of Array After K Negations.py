from collections import deque

nums =[3,-1,0,2]
k = 3

nums1=sorted(nums)
nums=deque(nums)
count=0
for i in nums1:
    if count==k:
        break
    if i<=0:
        nums.popleft()
        nums.append(abs(i))
    if i>0:
        nums.popleft()
        nums.append(i-(i*2))
    count+=1
print( (nums))