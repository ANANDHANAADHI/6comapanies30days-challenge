class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res = float('inf')
        d = {}
        j = 0
        for i in cards:
            if i in d:
                res = min(res,j-d[i])
                d[i] = j
            else:
                d[i] = j
            j+=1
        if res == float('inf'):
            return -1
        else:
            return res+1