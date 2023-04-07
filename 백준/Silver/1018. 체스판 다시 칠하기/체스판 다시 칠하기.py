n,m=map(int,input().split())
mindif=32
board=[]
for i in range(n):
    li=list(str(input()))
    board.append(li)
for nstart in range(0,n-7):
    for mstart in range(0,m-7):
        dif=0
        for line in range(nstart,nstart+8):
            for num in range(mstart,mstart+8):
                if (line+num)%2==0 and board[line][num]=='W':
                    dif+=1
                elif (line+num)%2==1 and board[line][num]=='B':
                    dif+=1
        if dif>32:
            dif=64-dif
        if dif<mindif:
            mindif=dif
print(mindif)