class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        from collections import defaultdict
        arr=defaultdict(int)

        answer=0
        count=0
        for i in range(len(nums)):
            count=0
            res=''
            for j in range(i,len(nums)):
                if nums[j]%p!=0:
                    res+=(str(nums[j])+'*')
                    if arr[res]==0:
                        answer+=1
                        arr[res]=1
                else:
                    count+=1
                    res += (str(nums[j])+'*')
                    if count<=k:
                        if arr[res] == 0:
                            answer += 1
                            arr[res] = 1
                    else:
                        break
        return answer