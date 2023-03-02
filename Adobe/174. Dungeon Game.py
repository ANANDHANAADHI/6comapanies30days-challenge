class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        mn = float('inf')
        def rec(i,j,sm,n):
            if i == n-1 and j == n-1:
                sm += dungeon[i][j]
                mn = min(abs(sm)+1,mn)
                print(mn)
                return
            if i > n-1 or j > n-1:
                return
            print(i,j , sm)
            sm += dungeon[i][j]
            rec(i,j+1,sm,n)
            rec(i+1,j,sm,n)
        rec(0,0,0,4)
        # print(mn)
        return 2