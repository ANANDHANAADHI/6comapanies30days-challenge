def getBiggestThree(self, grid):
    def calc(l, r, i, d):
        sum_ = 0
        c1 = c2 = (l + r) // 2 
        expand = True
        for row in range(i, d + 1):
            
            if c1 == c2:
                sum_ += grid[row][c1]
                
            else:
                sum_ += grid[row][c1] + grid[row][c2]
                
                
            if c1 == l:
                expand = False
                
            if expand:
                c1 -= 1
                c2 += 1
                
            else:
                c1 += 1
                c2 -= 1
                
        return sum_
        
        
        
        
    m = len(grid)
    n = len(grid[0])
    pq = []
    
    for i in range(m):
        for j in range(n):
            l = r = j
            d = i
            while l >= 0 and r <= n - 1 and d <= m - 1:
                sum_ = calc(l, r, i, d)
                l -= 1
                r += 1
                d += 2
                
                if len(pq) < 3:
                    if sum_ not in pq:
                        heapq.heappush(pq, sum_)
                
                else: 
                    if sum_ not in pq and sum_ > pq[0]:
                        heapq.heappop(pq)
                        heapq.heappush(pq, sum_)
                        
    pq.sort(reverse=True)                   
    return pq
                        
                    