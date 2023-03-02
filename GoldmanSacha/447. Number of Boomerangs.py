class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        distdict = defaultdict(lambda: defaultdict(list))
        for i in range(n):
            for j in range(n):
                dist = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                if i not in distdict[dist]:
                    distdict[dist][i] = [j]
                else:
                    distdict[dist][i].append(j)
        ans = 0
        for key in distdict:
            for pt in distdict[key]:
                nn = len(distdict[key][pt])
                ans += nn * (nn - 1)
        return ans