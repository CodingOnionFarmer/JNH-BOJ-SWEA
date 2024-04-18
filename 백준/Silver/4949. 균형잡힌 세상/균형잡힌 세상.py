while True:
    sent=str(input())
    if sent=='.':
        break
    sent=list(sent[:-1])
    key=True
    brackets=[]
    while sent!=[]:
        a=sent.pop()
        if a in [')',']']:
            brackets.append(a)
        elif a=='(':
            if brackets==[]:
                key=False
                break
            b=brackets.pop()
            if b==']':
                key=False
                break
        elif a=='[':
            if brackets==[]:
                key=False
                break
            b=brackets.pop()
            if b==')':
                key=False
                break
    if brackets!=[]:
        key=False
    if key:
        print('yes')
    else:
        print('no')