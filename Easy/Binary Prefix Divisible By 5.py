# class Solution:
#     def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
#         res=[]
#         x=''.join([str(x) for x in nums])
#         for i in range(len(nums)):
#             s1= int(x[:i+1],2)
#             if s1%5==0:
#                 res.append(True)
#             else:
#                 res.append(False)
#         return res

s=["123123"]
x=s.copy()
x.append(str(123))
print(s)