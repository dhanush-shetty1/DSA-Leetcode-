class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=nums[0]
        for i in range(1,len(nums)):
            ans+=nums[i]
            nums[i]=ans
        return nums
        