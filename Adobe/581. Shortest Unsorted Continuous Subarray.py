class Solution:
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        s_in = 0
        e_in  = 0
        i= 0
        j = 1
        t =0
        flag = True
        while(j<n):
            if nums[i] > nums[j]:
                if not flag :
                    s_in = t
                else:
                    s_in = i
                break 
            elif nums[i] == nums[j] and flag:
                t = i
                flag = False
                i+=1
                j+=1
            elif nums[i] < nums[j] and not flag:
                flag =True
                t =i
                i+=1
                j+=1
            else:
                flag =True
                i+=1
                j+=1
            # print(s_in)
        k = n-1
        l = n-2
        t = 0
        flag =True
        while(l>=0):
            if nums[k] < nums[l]:
                if not flag:
                    e_in = t
                    print("FF")
                else:
                    e_in = k
                print(k,"k")
                break
            elif nums[k] == nums[l] and flag:
                t = k
                flag = False
                k-=1
                l-=1
            elif nums[k] > nums[l] and not flag:
                flag =True
                t =k
                k-=1
                j-=1
            else:
                k-=1
                l-=1
        temp = max(e_in,s_in)-min(e_in,s_in)
        print(s_in,e_in)
        if temp == 0:
            return 0
        return temp+1
 
