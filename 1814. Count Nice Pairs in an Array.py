from collections import defaultdict as dd
class Solution:
    def countNicePairs(self, nums) -> int:
        res = 0
        x =len(nums)
        s =set()
        d =dd(int)
        for i in range(x):
            k =nums[i]- int(str(nums[i])[::-1])
            res+=d[k]
            d[k] +=1
        return res %1000000007
s =Solution()
l =list(map(int,input().split()))
print(s.countNicePairs(l))