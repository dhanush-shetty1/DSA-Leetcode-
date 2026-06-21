class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ans=0
        costs.sort()
        for num in costs:
            if coins>=num:
                coins-=num
                ans+=1
            else:
                break
        
        return ans
        
        