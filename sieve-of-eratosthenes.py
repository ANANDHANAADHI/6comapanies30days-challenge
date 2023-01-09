n = int(input())
f = [1] * n
for i in range(2,int(n**0.5)+1):
    if (f[i-1]):
        for j in range(i+i,n+1,i):
            f[j-1] = 0
a= [i for i in range(2,n+1) if f[i-1] ==1 ]
print(a)