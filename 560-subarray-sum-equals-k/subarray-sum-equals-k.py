from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp=defaultdict(int)
        mp[0]=1
        curr_sum=0
        count=0
        for num in nums:
            curr_sum+=num
            count+=mp[curr_sum-k]
            mp[curr_sum]+=1
        return count
