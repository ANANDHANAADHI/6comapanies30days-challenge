class Solution:
    def productx(self,lst,n):
        s = 0
        for i in range(1,n):
            s+= (i *lst[i])
        return s
    def maxRotateFunction(self, nums):
        n = len(nums)
        mx = self.productx(nums,n)
        for i in range(1,n):
            t = nums.pop()
            nums.insert(0,t)
            mx = max(mx,self.productx(nums,n))
        return mx
            