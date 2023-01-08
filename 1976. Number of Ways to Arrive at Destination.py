from collections import defaultdict
import math
import heapq
class Solution:
    def countPaths(self, n: int, roads) -> int:
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append([v, time])
            graph[v].append([u, time])

        def dijkstra(src):
            dist = [math.inf] * n
            ways = [0] * n
            minHeap = [(0, src)]  # dist, src
            dist[src] = 0
            ways[src] = 1
            while minHeap:
                # print(heappop(minHeap))
                d, u = heapq.heappop(minHeap)
                # print(d,u)
                if dist[u] < d: continue  # Skip if `d` is not updated to latest version!
                for v, time in graph[u]:
                    if dist[v] > d + time:
                        dist[v] = d + time
                        ways[v] = ways[u]
                        heapq.heappush(minHeap, (dist[v], v))
                    elif dist[v] == d + time:
                        ways[v] = (ways[v] + ways[u]) % 1_000_000_007
            return ways[n - 1]

        return dijkstra(0)
s = Solution()
n = int(input())
l = []
for i in range(n+3):
    l.append(list(map(int,input().split())))
print(s.countPaths(n,l))