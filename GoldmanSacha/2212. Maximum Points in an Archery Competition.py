class Solution:
  def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
    ##
    def dp(st,arr):
      if st == 12 or arr == 0:
        return 0
      mS = dp(st+1,arr)
      if aliceArrows[st] < arr:
        return max(mS,dp(st+1,arr-aliceArrows[st]-1) + st)
      else:
        return mS
    ##
    ans = [0]*12
    remarr = numArrows
    for ii in range(12):
      if dp(ii+1,remarr) < dp(ii,remarr):
        ans[ii] = aliceArrows[ii] + 1
        remarr -= aliceArrows[ii] + 1
    ans[0] += remarr
    return ans