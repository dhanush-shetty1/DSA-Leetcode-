from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_e=0
        result=0
        hashmap=defaultdict(int)

        for num in nums:
            hashmap[num]+=1
        for num in nums:
            if hashmap[num]>max_e:
                max_e=hashmap[num]
                result=num
        return result
        