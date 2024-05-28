def solution(brown, yellow):
    answer = [2 + brown // 2] * 2
    discriminant = answer[0] ** 2 - 4 * (brown + yellow)
    if discriminant:
        root = int((discriminant + 1)**0.5)
        answer[0] += root
        answer [1] -= root
    answer[0] //= 2
    answer[1] //= 2
    return answer