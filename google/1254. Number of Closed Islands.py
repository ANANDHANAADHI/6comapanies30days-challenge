class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        # go through the grid and make a dfs per island
        result = 0
        m = len(grid)
        n = len(grid[0])
        for rx in range(m):
            for cx in range(n):

                # check whether we found an island
                if grid[rx][cx] == 0 and self.islandDfs(rx, cx, grid, m, n):
                    result += 1
        return result
    

    def islandDfs(self, rx, cx, grid, m, n):
        
        # check whether we are out of bounds
        if rx < 0 or cx < 0 or rx >= m or cx >=n:
            return False
        
        # check whether we are water
        if grid[rx][cx] == 1:
            return True
        
        # check whether we already visited
        if grid[rx][cx] == -1:
            return True

        # set ourself to visited
        grid[rx][cx] = -1

        # traverse in all directions
        result = True
        for rx, cx in [(rx-1, cx), (rx+1, cx), (rx, cx-1), (rx, cx+1)]:
            if not self.islandDfs(rx, cx, grid, m, n):
                result = False
        
        # check all sourrounding cells
        return result