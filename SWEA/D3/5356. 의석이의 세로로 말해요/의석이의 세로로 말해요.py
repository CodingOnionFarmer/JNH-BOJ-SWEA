t = int(input())
for tc in range(1, t + 1):
    print(f'#{tc} ', end='')
    words = [input() for _ in range(5)]
    for i in range(max(len(word) for word in words)):
        for j in range(5):
            try:
                print(words[j][i],end='')
            except:
                pass
    print()
