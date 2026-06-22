from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = defaultdict(int)

        for ch in text:
            hashmap[ch] += 1

        return min(
            hashmap["b"],
            hashmap["a"],
            hashmap["l"] // 2,
            hashmap["o"] // 2,
            hashmap["n"],
        )
