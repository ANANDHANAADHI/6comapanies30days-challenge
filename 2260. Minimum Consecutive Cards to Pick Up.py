class Solution:
    def minimumCardPickup(self, cards) -> int:
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
s = Solution()
l =list(map(int,input().split()))
print(s.minimumCardPickup(l))