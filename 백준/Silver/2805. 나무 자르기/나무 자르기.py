import sys
n,m=map(int,input().split())
trees=list(map(int,sys.stdin.readline().split()))
trees.sort()
s=sum(trees)
ex_tree=0
for tree in trees:
    s-=(tree-ex_tree)*n
    if s<m:
        low=ex_tree
        high=tree
        break
    ex_tree=tree
    n-=1
print(high-(m-s+n-1)//n)