class Solution:
    def maxCoins(self, piles) -> int:
        piles.sort(reverse=True)
        return sum(piles[i] for i in range(1, 2 * len(piles) // 3 + 1, 2))