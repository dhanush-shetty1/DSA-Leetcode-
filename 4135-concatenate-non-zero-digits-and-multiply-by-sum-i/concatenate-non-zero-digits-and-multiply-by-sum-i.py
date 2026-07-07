class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        l=str(n)
        x=""
        add=0

        for ch in l:
            if ch!='0':
                x+=ch
                add+=int(ch)
        
        x=int(x)
        x=x*add
        return x

        
        