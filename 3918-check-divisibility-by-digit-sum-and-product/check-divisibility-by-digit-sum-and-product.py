class Solution:
    def checkDivisibility(self, n: int) -> bool:
        mult=1
        suma=0
        digit=n

        while digit!=0:
            suma+=digit%10
            mult*=digit%10
            digit=digit//10
        
        return n%(suma+mult)==0
        