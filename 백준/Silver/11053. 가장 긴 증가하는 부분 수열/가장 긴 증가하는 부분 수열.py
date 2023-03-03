n = int(input())
lst = list(map(int, input().split()))
stack = [0]
for i in lst:
    if i > stack[-1]:
        stack.append(i)
        continue
    for j in range(len(stack)):
        if i > stack[len(stack) - 1 - j]:
            stack[len(stack) - j] = i
            break
print(len(stack) - 1)
