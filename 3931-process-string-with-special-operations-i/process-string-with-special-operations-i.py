class Solution:
    def processStr(self, s: str) -> str:
        result=""
        special=["%","*","#"]
        for i in range(len(s)):
            if s[i] not in special:
                result+=s[i]
            elif s[i]=="#":
                result+=result
            elif s[i]=="%":
                result=result[::-1]
            else:
                result=list(result)
                if len(result)<=0:
                    pass
                else:
                    result.pop(-1)
                result="".join(result)
        return result

        