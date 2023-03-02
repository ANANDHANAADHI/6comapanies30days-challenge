class Solution:
    import random
    def __init__(self, w: List[int]):
        self.total = sum(w)
        self.cumlst = []
        cum = 0
        for ele in w:
            cum += ele/self.total
            self.cumlst.append(cum)
        

    def pickIndex(self) -> int:
        r_v = random.random()
        
        return bisect_left(self.cumlst, r_v)
