class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window=nums[0:k]
        curr=sum(window)
        ans=curr

        for i in range(len(nums)-k):
            curr=curr-nums[i]+nums[i+k]
            ans=max(ans,curr)
        
        return ans/k
        
        