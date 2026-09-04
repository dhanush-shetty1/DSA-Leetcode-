class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        for i in range(len(nums)):
            temp1=nums[:i+1]
            temp2=nums[i:len(nums)]
            a=max(temp1)
            b=min(temp2)
            s=a-b
            if s<=k:
                return i
        return -1