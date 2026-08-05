class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=""
        for ch in s:
            if ch.isalnum():
                ans+=ch.lower()
        
        if ans[::-1]==ans:
            return True
        
        return False
        