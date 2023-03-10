class Solution:
    def largestDivisibleSubset(self, nums):
        S = {-1: set()}
        for x in sorted(nums):
            S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
        return list(max(S.values(), key=len))
s = Solution()
l = list(map(int,input().split()))
print(s.largestDivisibleSubset(l))