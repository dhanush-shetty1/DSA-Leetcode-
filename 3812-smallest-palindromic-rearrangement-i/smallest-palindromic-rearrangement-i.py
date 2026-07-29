from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq=Counter(s)
        left=[]
        mid=""

        for ch in sorted(freq):
            if freq[ch]%2:
                mid=ch
            
            left.append(ch*(freq[ch]//2))

        left="".join(left)
        return left + mid + left[::-1]



        