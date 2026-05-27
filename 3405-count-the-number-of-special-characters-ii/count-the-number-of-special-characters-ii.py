class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = {}
        upper = {}

        for i in range(len(word)):

            if word[i].islower():
                lower[word[i]] = i

            else:

                ch = word[i].lower()
                if ch not in upper:
                    upper[ch] = i

        count = 0

        for ch in lower:

            if ch in upper and lower[ch] < upper[ch]:
                count += 1

        return count