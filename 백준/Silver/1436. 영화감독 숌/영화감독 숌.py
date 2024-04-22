n=int(input())
endnumbers=[]
a=666
while len(endnumbers)<n:
    w=str(a)
    if '666' in w:
        endnumbers.append(a)
    a+=1
print(endnumbers[n-1])