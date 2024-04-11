def solution(scores):
    n = len(scores)
    wanho = [scores[0][i] for i in range(2)]
    ws = sum(wanho)
    sido = [[] for _ in range(100001)]  # scores in descending order
    for i in range(n):
        was, prs = scores[i][0], scores[i][1]  # working attitude score, peer review score
        sido[was].append(prs)
    for j in range(100001):
        sido[j].sort(reverse = True)
    hprs = 0  # highest peer review score
    was = 100000
    rank = 1
    while was > wanho[0]:
        if sido[was]:
            temp_hprs = sido[was][0]
            for prs in sido[was]:
                if prs >= hprs:
                    if prs + was > ws:
                        rank += 1
                else:
                    break
            if temp_hprs > hprs:
                hprs = temp_hprs
        was -= 1
    if wanho[1] < hprs:
        rank = -1
    else:
        while was > -1:
            if sido[was]:
                temp_hprs = sido[was][0]
                for prs in sido[was]:
                    if prs >= hprs:
                        if prs + was > ws:
                            rank += 1
                    else:
                        break
                if temp_hprs > hprs:
                    hprs = temp_hprs
            was -= 1
    answer = rank
    return answer