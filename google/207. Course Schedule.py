class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)
        visited = [False for i in range(numCourses)]

        def dfs(node):
            if not visited[node]:
                visited[node] = True
                for i in adj[node]:
                    if dfs(i):
                        return True
                visited[node] = False
                return False
            return True
        for i in range(numCourses):
            if dfs(i):
                return False
        return True
