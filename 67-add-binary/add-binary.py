class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def dec(x):
            count=0
            num=0

            for i in range(len(x)-1,-1,-1):
                if x[i]=='1':
                    num+=2**count
                    count+=1
                else:
                    count+=1
            
            return num
        
        def bina(x):
            if x==0:
                return "0"
            
            ans=""

            while x>0:
                rem=x%2
                ans=str(rem)+ans
                x=x//2
            
            return ans
        
        a=dec(a)
        b=dec(b)
        c=a+b
        return bina(c)