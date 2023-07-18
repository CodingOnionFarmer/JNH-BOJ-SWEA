a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
w=str(input())
w=w.upper()
l=[]
for i in range(26):
    l.append(w.count(a[i]))
sl=sorted(l)
if sl[24]==sl[25]:
    print('?')
else:
    print(a[l.index(max(l))])