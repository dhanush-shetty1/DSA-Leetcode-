class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m=max(nums)
        L=[]
        for i in range(1,m+1):
            L.append(i)
        L.append(m)

        if len(L)!=len(nums):
            return False
        nums.sort()
        return nums==L




        