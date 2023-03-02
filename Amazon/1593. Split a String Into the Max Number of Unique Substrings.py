from collections import defaultdict as dd
class Solution:
    def maxUniqueSplit(self, st: str) -> int:
        s = set()
        return self.func(st, s)

    def func(self, st, s):
        ans = 0
        if st:
            for i in range(1, len(st) + 1):
                candidate = st[:i]
                if candidate not in s:
                    s.add(candidate)
                    ans = max(ans, 1 + self.func(st[i:], s))
                    s.remove(candidate)
        return ans

s =Solution()
print(s.maxUniqueSplit(input()))