class Solution:
    def rotatedDigits(self, n: int) -> int:
        good = {2,5,6,9}
        valid = {0,1,2,5,6,8,9}
        
        count = 0
        
        for i in range(1, n+1):
            num = i
            changed = False
            
            while num > 0:
                digit = num % 10
                
                if digit not in valid:
                    break
                
                if digit in good:
                    changed = True
                
                num //= 10
            else:
                if changed:
                    count += 1
        
        return count