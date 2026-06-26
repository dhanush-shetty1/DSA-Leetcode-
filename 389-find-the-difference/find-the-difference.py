from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        l=defaultdict(int)
        
        for ch in s:
            l[ch]+=1

        for ch in t:
            l[ch]-=1

            if l[ch]<0:
                return ch