class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        dp, ct = [0] * n, 0
        dp[0] = 1
        for i in range(1, n):

            dp[i] = ct + dp[i-delay] - dp[i-forget]
            ct = dp[i]
            # print(dp,ct)

        return sum(dp[n-forget:]) % 1000000007