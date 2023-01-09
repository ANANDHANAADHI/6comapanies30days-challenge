class Solution:
    def fact(self,n):
        if n ==0:
            return 1
        else:
            return n*self.fact(n-1)
    def trailingZeroes(self, n: int) -> int:
        s = self.fact(n)
        ans = 0
        while(True):
            if s%10 == 0:
                ans+=1
                s = s//10
            else:
                break

        return ans