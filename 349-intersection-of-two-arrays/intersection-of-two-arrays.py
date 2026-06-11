class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        L = set()

        for j in range(len(nums2)):
            if nums2[j] in nums1:
                L.add(nums2[j])

        return list(L)
        