class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        M=0

        for arr in accounts:
            curr=sum(arr)
            M=max(curr,M)
        
        return M