class Solution:
    def maxMatrixSum(self, matrix) -> int:
        mn_cnt = 0
        mn = float('inf')
        sm = 0
        for i in matrix:
            for j in i:
                if j < 0:
                    mn_cnt+=1
                if mn > abs(j):
                    mn = abs(j)
                sm+=abs(j)
        if mn_cnt %2 ==0:
            return sm
        else:
            return sm-mn-mn
s = Solution()
l = []
row = input()
for  i in range(row):
    l.append(list(map(int,input().split())))
print(s.maxMatrixSum(l))