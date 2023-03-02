class Solution:
    def fact(self,n):
        if n ==0:
            return 1
        else:
            return n*self.fact(n-1)
    def trailingZeroes(self, n: int) -> int:
    #    print(self.fact(n))
       ans = n//5
       a = ans
       while(True):
        ans+= a//5
        if a//5 <5:
            break
        a = a//5
       return ans
s = Solution()
n =int(input())
print(s.trailingZeroes(n))