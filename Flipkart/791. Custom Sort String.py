from collections import defaultdict as dd
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = dd(int)
        st = ''
        f =''
        d1 = dd(int)
        for k in order:
            d1[k]+=1
        for i in s:
            if i in d1:
                d[i] +=1
            else:
                f+=i
        for j in order:
            if d[j] > 0:
                st+=(j*d[j])
        return st+f
