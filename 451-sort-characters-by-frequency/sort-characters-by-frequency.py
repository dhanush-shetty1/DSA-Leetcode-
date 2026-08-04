from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap=defaultdict(int)
        for ch in s:
            hashmap[ch]+=1
        
        order=sorted(hashmap,key=hashmap.get,reverse=True)
        ans=""
        for ch in order:
            ans+=ch*hashmap[ch]
        return ans
