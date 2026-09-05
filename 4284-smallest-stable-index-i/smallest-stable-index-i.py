class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        for i in range(len(nums)):
            temp1=max(nums[:i+1])
            temp2=min(nums[i:len(nums)])
            if temp1-temp2<=k:
                return i
        return -1