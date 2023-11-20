import sys
m=int(input())
s=set()
for i in range(m):
    command=str(sys.stdin.readline().strip())
    initial=command[:2]
    if initial=='ad':
        s.add(int(command[-2:]))
    elif initial=='re':
        s.discard(int(command[-2:]))
    elif initial=='ch':
        if int(command[-2:]) in s:
            print(1)
        else:
            print(0)
    elif initial=='to':
        if int(command[-2:]) in s:
            s.discard(int(command[-2:]))
        else:
            s.add(int(command[-2:]))
    elif initial=='al':
        s={i+1 for i in range(20)}
    else:
        s=set()