class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=nums[:n]
        y=nums[n:len(nums)]

        a=0
        b=0

        for i in range(len(nums)):
            if i%2==0:
                nums[i]=x[a]
                a+=1
            else:
                nums[i]=y[b]
                b+=1
        
        return nums
        