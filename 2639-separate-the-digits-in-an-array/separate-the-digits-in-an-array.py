class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        L=[]    

        for num in nums:
            temp=[]
            while num!=0:
                temp.append(num%10)
                num=num//10
            L.extend(temp[::-1])

        return L

        