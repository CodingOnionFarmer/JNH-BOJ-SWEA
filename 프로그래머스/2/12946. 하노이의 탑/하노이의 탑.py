def solution_from_a_to_b(n,a,b):
    if n == 1:
        return [[a,b]]
    c = 6 - a - b
    return solution_from_a_to_b(n-1,a,c) + [[a,b]] + solution_from_a_to_b(n-1,c,b)


def solution(n):
    return solution_from_a_to_b(n,1,3)