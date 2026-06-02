from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap=defaultdict(int)

        for i in range(len(nums)):
            hashmap[nums[i]]+=1

        for i in range(len(nums)):
            if hashmap[nums[i]]==1:
                return nums[i]
        