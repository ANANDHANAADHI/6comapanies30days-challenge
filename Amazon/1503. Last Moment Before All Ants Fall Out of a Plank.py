class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
                return max(0, max(left + [0]), n - min(right + [n]))