class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        @functools.lru_cache(None)
        def solve(N,K,r,c):
            if(r < 0 or r > N - 1 or c < 0 or c > N - 1):
                return 0
            if K==0:
                return 1
            rate=0
            for i in dir:
                rate+=0.125 * solve(N,K-1,r+i[0],c+i[-1])
            return rate
        dir=[[-2,-1],[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1]]
        return solve(N,K,r,c)
        