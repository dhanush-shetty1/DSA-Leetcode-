from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap=defaultdict(int)

        for num in nums1:
            hashmap[num]+=1

        ans=[]

        for num in nums2:
            if hashmap[num]>0:
                ans.append(num)
                hashmap[num]-=1
        
        return ans
        