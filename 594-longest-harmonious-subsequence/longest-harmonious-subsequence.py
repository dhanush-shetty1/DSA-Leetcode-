from collections import defaultdict
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        mp=defaultdict(int)

        for num in nums:
            mp[num]+=1
        ans=0
        for num in nums:
            if num+1 in mp:
                ans=max(ans,mp[num]+mp[num+1])
        return ans

        