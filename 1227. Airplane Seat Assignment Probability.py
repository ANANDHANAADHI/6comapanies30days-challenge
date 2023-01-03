class Solution:
    def nthPersonGetsNthSeat(self, n):
        if n == 1:
            return 1
        return 0.5
s = Solution()
print(s.nthPersonGetsNthSeat(int(input())))