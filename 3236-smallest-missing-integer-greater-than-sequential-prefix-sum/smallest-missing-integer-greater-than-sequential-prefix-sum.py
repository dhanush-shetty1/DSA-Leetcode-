class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total=nums[0]

        for i in range(1,len(nums)):
            if nums[i-1]+1==nums[i]:
                total+=nums[i]
            else:
                break
        
        while total in nums:
            total+=1
        
        return total
