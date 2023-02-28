t = int(input())
decode = [9, 0, 6, 5, 2, 4, 8, 1, 7, 3]
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    total = 0
    checkpoint = {}
    for i in range(n):
        num = input()
        new_checkpoint = {}
        if int(num, 16):
            end = m - 1
            shift = 0
            while True:
                found = False
                for j in range(end, -1, -1):
                    # print(i, end, j, num[j],shift, checkpoint)
                    if int(num[j], 16):
                        found = True
                        if j in checkpoint:
                            new_checkpoint[j] = checkpoint[j]
                            end = checkpoint[j]
                            k = int(num[j], 16)
                            k >> shift
                            while not k % 2:
                                k //= 2
                                shift += 1
                            break
                        if j == end and shift and not int(num[j], 16) >> shift:
                            found = False
                            shift = 0
                            continue
                        c = 0
                        check = int(num[max(0,j - 63):j + 1], 16)
                        while not check % 2:
                            check //= 2
                        check = bin(check)
                        p = len(check) - 1
                        # print(check)
                        while int(check[p]):
                            p -= 1
                            c += 1
                        while not int(check[p]):
                            p -= 1
                            c += 1
                        while int(check[p]):
                            p -= 1
                            c += 1
                        while not int(check[p]):
                            p -= 1
                            c += 1
                        expand = c // 7
                        new_checkpoint[j] = j - 2 * c
                        end = new_checkpoint[j]
                        # print(num[j - 2 * c:j + 1])
                        hd_code = int(num[j - 2 * c:j + 1], 16)
                        if j == end and shift:
                            hd_code >> shift
                        while not hd_code % 2:
                            hd_code //= 2
                            shift += 1
                        hd_code = bin(hd_code)[2:]
                        if len(hd_code) > 56 * expand:
                            hd_code = hd_code[len(hd_code) - 56 * expand:]
                        else:
                            hd_code = '0' * (56 * expand - len(hd_code)) + hd_code
                        # print(hd_code)
                        # print(shift)
                        # print(expand)
                        code_sum = verify = 0
                        for k in range(8):
                            code = ''
                            for l in range(7):
                                code += hd_code[(k * 7 + l) * expand]
                            code = int(code[2:6], 2) - 5
                            if code < 0:
                                code = 5
                            real = decode[code]
                            code_sum += real
                            verify += real * (3 - (k % 2 * 2))
                        if verify % 10:
                            code_sum = 0
                        total += code_sum
                        # print(end, j, c)
                        break
                if not found:
                    break
        checkpoint = new_checkpoint
    print(f'#{tc}', total)
