class Solution:
    def reverseWords(self, s: str) -> str:
        ans=" ".join(word[::-1] for word in s.split())

        return ans
        