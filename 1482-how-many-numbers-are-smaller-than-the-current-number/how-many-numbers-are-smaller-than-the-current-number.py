class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        j=0

        for i in range(len(nums)):
            count=0
            while j<len(nums):
                if nums[i]>nums[j]:
                    count+=1
                    j+=1
                else:
                    j+=1
            ans.append(count)
            j=0
        return ans