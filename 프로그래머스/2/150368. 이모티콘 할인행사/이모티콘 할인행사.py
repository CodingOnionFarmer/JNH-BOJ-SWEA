def solution(users, emoticons):
    answer = [0,0]
    n = len(users)
    m = len(emoticons)
    discounted = [[] for _ in range(m)]
    for i in range(m):
        pdt = emoticons[i] // 10  # price divided by ten
        for j in range(9, 5, -1):
            discounted[i].append(pdt*j)
    for code in range(4**m):  # 4진수 코드, 1330이면 각 이모티콘을 20%, 40%, 40%, 10% 할인하기
        membership = 0
        sales = 0
        price_rate = []
        for i in range(m):
            price_rate.append(code%4)  # price_rate가 0면 10%, 1이면 20%, 2이면 30%, 3이면 40%할인
            code //= 4
        for ratio, price in users:
            bought = 0
            for i in range(m):
                if price_rate[i] * 10 + 10 >= ratio:
                    bought += discounted[i][price_rate[i]]
            if bought >= price:
                membership += 1
            else:
                sales += bought
        if membership > answer[0]:
            answer[0] = membership
            answer[1] = sales
        elif membership == answer[0] and sales > answer[1]:
            answer[1] = sales
    return answer