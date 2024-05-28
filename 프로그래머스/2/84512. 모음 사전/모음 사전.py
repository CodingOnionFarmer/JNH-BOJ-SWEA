def solution(word):
    alp = {'A' : 0, 'E' : 1, 'I' : 2, 'O' : 3, 'U' : 4}
    tail = [1, 6, 31, 156, 781]
    answer = 0
    for i in range(len(word)):
        answer += 1
        answer += alp[word[i]] * tail[4 - i]
    return answer