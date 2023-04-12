n = int(input())
arr = list(map(int, input().split()))
rev = list(reversed(arr))
longest = []
longest_rev = []
stack = [0]
stack_rev = [0]
for i in arr:
    if i > stack[-1]:
        stack.append(i)
    else:
        for j in range(1, len(stack)):
            if i > stack[len(stack) - 1 - j]:
                stack[len(stack) - j] = i
                break
    longest.append(len(stack) - 1)
for i in rev:
    if i > stack_rev[-1]:
        stack_rev.append(i)
    else:
        for j in range(1, len(stack_rev)):
            if i > stack_rev[len(stack_rev) - 1 - j]:
                stack_rev[len(stack_rev) - j] = i
                break
    longest_rev.append(len(stack_rev) - 1)
longest_rev.reverse()
print(max(longest[i] + longest_rev[i] for i in range(n)) - 1)
