from collections import defaultdict
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        hashmap=defaultdict(int)

        for num in nums1:
            if num not in hashmap:
                hashmap[num]+=1
        
        for num in nums2:
            hashmap[num]+=1

        for num in hashmap:
            if hashmap[num]>1:
                return num
        return -1
        