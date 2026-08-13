class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for ch in words:
            if ch==ch[::-1]:
                return ch
        return ""

        