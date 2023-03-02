class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        S=statements
        n=len(S)
        pop=(1<<n)*[0]
        f0=(1<<n)*[0]
        f1=(1<<n)*[0]
        for i in range(n):
            k=1<<i
            pop[k]=1
            x0=f0[k]=sum(1<<j for j in range(n) if S[i][j]==0) # people who are Forced to be bad if person i is truthful
            x1=f1[k]=sum(1<<j for j in range(n) if S[i][j]==1) # people who are Forced to be good if person i is truthful
            for j in range(1,k):
                k+=1
                pop[k]=pop[j]+1
                f0[k]=f0[j]|x0
                f1[k]=f1[j]|x1
        return max(pop[i] for i in range(1<<n) if i&f0[i]==0 and i|f1[i]==i)