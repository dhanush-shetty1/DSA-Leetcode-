class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        def product(num):
            ans = 1

            while num > 0:
                ans *= num % 10
                num //= 10

            return ans
            
        while True:

            if product(n) % t == 0:
                return n

            n += 1