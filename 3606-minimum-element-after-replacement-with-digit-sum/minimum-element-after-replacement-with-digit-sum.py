class Solution:
    def minElement(self, nums: List[int]) -> int:

        for i in range(len(nums)):

            total = 0
            num = nums[i]

            while num != 0:
                digit = num % 10
                total += digit
                num = num // 10

            nums[i] = total

        return min(nums)