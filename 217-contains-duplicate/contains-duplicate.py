from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap=defaultdict(int)

        for num in nums:
            if num in hashmap:
                return True
            hashmap[num]+=1
        
        return False
        
        
        