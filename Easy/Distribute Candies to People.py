class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res=[0]*num_people
        i=1
        j=0
        while(candies):
            if(candies<i):
                res[j%num_people]+=candies
                break
            if(candies>=i):
                res[j%num_people]+=i
                candies-=i
                j+=1
                i+=1
            
        return(res)