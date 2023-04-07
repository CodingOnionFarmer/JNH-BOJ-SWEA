n=123456*2
a = [False,False] + [True]*(n-1)
primes=[]
for i in range(2,n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
n=int(input())
while n>0:
    print(len(list(x for x in primes if n<x<n*2+1)))
    n=int(input())