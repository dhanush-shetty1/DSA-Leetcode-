class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans=float('INF')

        for i in range(len(nums)):
            ans=min(ans,nums[i])

        return ans


        