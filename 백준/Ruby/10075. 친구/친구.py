n = int(input())
original = list(map(int, input().split()))
# with i , without i
score = [[i, 0] for i in original]
ho_pro = list(map(int, input().split()))
for i in range(n - 1, 0, -1):
    ho, pro = ho_pro[2 * i - 2], ho_pro[2 * i - 1]
    if not pro:
        score[ho][0] += score[i][1]
        score[ho][1] += score[i][0]
    elif pro == 1:
        score[ho][0] += score[i][0]
        score[ho][1] += score[i][1]
    else:
        score[ho][0] = max(score[ho][0], score[i][0])
        score[ho][1] = max(score[ho][1], score[i][1])
print(max(score[0]))
