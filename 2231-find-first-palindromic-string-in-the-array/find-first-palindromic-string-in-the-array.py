class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        for ch in words:
            left=0
            right=len(ch)-1

            while left<right:
                if ch[left]!=ch[right]:
                    break
                left+=1
                right-=1

            if left>=right:
                return ch
        return ""

        