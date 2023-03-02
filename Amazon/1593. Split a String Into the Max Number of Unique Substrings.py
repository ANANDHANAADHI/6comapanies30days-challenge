from collections import defaultdict as dd
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        d = dd(int)
        res = 0
        j = 0
        i = 0
        while(j<=len(s)):
            if d[s] 

