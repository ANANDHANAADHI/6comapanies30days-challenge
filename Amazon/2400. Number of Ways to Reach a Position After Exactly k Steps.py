class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        d = abs(endPos-startPos)
        if k == d: return 1
        elif k < d or (k-d)&1: return 0
        return comb(k, (k-d)//2) % (10**9 + 7)