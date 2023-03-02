class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        l = []
        am = float('inf')
        for i in special:
            flag =True
            for j in range(len(i)-1):
                if needs[j] < i[j]:
                    flag = False
                    break
            if flag :
                l.append(i)
        for k in l:
            ln = len(k)
            a = k[ln-1]
            for t in range(ln-1):
                a+= (needs[t]-k[t])*price[t]
            if am > a:
                am = a
        if sum(needs) == 0 or sum(price) == 0:
            return 0
        return am
                
                
            

