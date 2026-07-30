class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashmap = {}

        for i in range(len(list2)):
            hashmap[list2[i]] = i

        minimum = float("inf")
        ans = []

        for i in range(len(list1)):

            if list1[i] in hashmap:

                curr = i + hashmap[list1[i]]

                if curr < minimum:
                    minimum = curr
                    ans = [list1[i]]

                elif curr == minimum:
                    ans.append(list1[i])

        return ans