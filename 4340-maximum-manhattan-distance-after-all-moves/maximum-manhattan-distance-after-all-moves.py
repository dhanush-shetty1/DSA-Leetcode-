class Solution:
    def maxDistance(self, moves: str) -> int:
        R = moves.count('R')
        L = moves.count('L')
        U = moves.count('U')
        D = moves.count('D')
        B = moves.count('_')

        return abs(R - L) + abs(U - D) + B