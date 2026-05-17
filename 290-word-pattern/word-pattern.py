class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        map1={}
        map2={}

        if len(pattern)!=len(words):
            return False

        for i in range(len(pattern)):
            p=pattern[i]
            w=words[i]

            if p in map1 and map1[p]!=w:
                return False
            if w in map2 and map2[w]!=p:
                return False
            map1[p]=w
            map2[w]=p
        
        return True

            

        