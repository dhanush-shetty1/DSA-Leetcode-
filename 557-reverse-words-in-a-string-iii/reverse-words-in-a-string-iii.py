class Solution:
    def reverseWords(self, s: str) -> str:
        word=""
        ans=""
        for i in range(len(s)):
            if s[i]!=" ":
                word+=s[i]
            else:
                ans+=word[::-1]
                ans+=" "
                word=""
        
        return ans+word[::-1]
        