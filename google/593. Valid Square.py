class Solution:
    s =set()
    def calcdist(self,a,b):
        self.s.add((a[0]-b[0])**2 + (a[1]-b[1])**2)
        print(self.s)

    def validSquare(self, p1 ,p2,p3,p4) -> bool:
        self.s = set()
        self.calcdist(p1,p2)
        self.calcdist(p1,p3)
        self.calcdist(p1,p4)
        self.calcdist(p3,p4)
        self.calcdist(p2,p3)
        self.calcdist(p2,p4)
        
        if len(self.s) ==2 and 0 not in self.s: 
            return True
        else:
            return False
s = Solution()
l = []
for i in range(4):
    l.append(list(map(int,input().split())))
print(s.validSquare(l[0],l[1],l[2],l[3]))