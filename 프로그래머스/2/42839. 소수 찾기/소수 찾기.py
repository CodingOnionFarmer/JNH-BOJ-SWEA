from itertools import permutations

def solution(numbers):
    answer = 0
    primes = [i for i in range(2,10000) if not {j for j in range(2,100) if not i%j and i!=j}]
    number = {int(''.join(p)[:k+1]) for p in permutations(numbers) for k in range(len(numbers))}
    answer = len({number for number in number if not {prime for prime in primes if not number%prime and number!=prime}} - {0,1})
    return answer