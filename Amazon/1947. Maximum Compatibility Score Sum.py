class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        return self.mySoldfs(students, mentors, set(), 0)
        
    def mySoldfs(self, students, mentors, hashSet, indS):
        if indS>=len(students):
            return 0
        res=0
        maxx=0
        for i in range(len(mentors)):
            if i not in hashSet:
                res = self.match(students[indS], mentors[i])
                hashSet.add(i)
                maxx = max(maxx, res+self.mySoldfs(students, mentors, hashSet, indS+1))
                hashSet.remove(i)
        return maxx
    
    def match(self, x, y):
        res=0
        i=j=0
        while(i<len(x)and j<len(y)):
            if x[i]==y[j]:
                res+=1
            i+=1;
            j+=1;
        return res
            