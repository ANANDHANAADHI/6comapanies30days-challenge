class Solution:
    def trailingZeroes(self, n: int) -> int:
       ans = n//5
       a = ans
       while(True):
        ans+= a//5
        if a//5 <5:
            break
        a = a//5
       return ans