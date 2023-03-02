from collections import defaultdict as dd
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = dd(int)
        res = []
        words.sort()
        for i in words:
            d[i] +=1
        # print(d)
        l = [ke for ke, va in (sorted(d.items(), key=lambda item: item[1]))]
        f = [va for ke, va in reversed(sorted(d.items(), key=lambda item: item[1]))]
        # print(l)
        # l = l[len(l)-k:]
        f = list(set(f[:k]))
        f.sort(reverse=True)
        # print(l) 
        for j in range(len(f)):
            for x in l:
                if d[x] == f[j]:
                    res.append(x)
        return res[:k]

