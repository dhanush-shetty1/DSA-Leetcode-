from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)

        for ch in strs:
            key="".join(sorted(ch))
            hashmap[key].append(ch)
        return list(hashmap.values())

        
        