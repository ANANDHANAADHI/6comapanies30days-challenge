class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        memo = dict()
        for x,y,z in flights:
            if x in graph:
                graph[x].append((y,z))
            else:
                graph[x] = [(y,z)]

        def f(cur,k):
            if (cur,k) in memo: return memo[(cur,k)]
            if cur == dst:return 0
            if cur not in graph or k == 0: return float("inf")
            
            best = float("inf")
            for node,price in graph[cur]:
                best = min(best,f(node,k-1) + price)
            
            memo[(cur,k)] = best
            return memo[(cur,k)]

        res = f(src,k+1)
        if res == float("inf"): res = -1

        return res
    