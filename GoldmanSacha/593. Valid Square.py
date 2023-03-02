class Solution:
    s =set()
    def calcdist(self,a,b):
        self.s.add((a[0]-b[0])**2 + (a[1]-b[1])**2)
        # print(self.s)

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        self.s = set()
        self.calcdist(p1,p2)
        self.calcdist(p1,p3)
        self.calcdist(p1,p4)
        self.calcdist(p3,p4)
        self.calcdist(p2,p3)
        self.calcdist(p2,p4)
        
        if len(self.s) ==2 and 0 not in self.s: 
            # print(self.s)
            return True
        else:
            return False