from collections import defaultdict
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans=[]
        hashmap=defaultdict(int)
        n=len(nums)
        for num in nums:
            hashmap[num]+=1
        
        for i in range(1,n+1):
            if hashmap[i]==0:
                ans.append(i)
        
        return ans
        

        