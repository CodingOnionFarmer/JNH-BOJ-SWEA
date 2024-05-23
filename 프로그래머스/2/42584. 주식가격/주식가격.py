def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    for i in range(n):
        price = prices[i]
        while stack:
            if stack[-1][0] > price:
                idx = stack[-1][1]
                answer[idx] = i - idx
                stack.pop()
            else:
                break
        stack.append((price, i))
    for j in range(len(stack)):
        idx = stack[j][1]
        answer[idx] = n - idx - 1
    return answer