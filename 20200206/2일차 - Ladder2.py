import sys
sys.stdin = open('2일차 - Ladder2.txt', 'r')

T = int(input())
# idy, idx
R = [0, 1]
L = [0, -1]
D = [1, 0]


for tc in range(T):
    ladder = []
    for _ in range(100):
        ladder.append(list(map(int,input().split())))
    # print(ladder)

    dic = {}
    for i in range(100):
        if ladder[0][i] == 1:
            x = i
            y = 0
            d = 0
            count = 0
            while y < 99:
                if x == 0:
                    if ladder[y+R[0]][x+R[1]] == 1:
                        y = y+R[0]
                        x = x+R[1]
                        d = 1
                        count += 1
                    elif ladder[y+D[0]][x+D[1]] == 1:
                        y = y + D[0]
                        x = x + D[1]
                        d = 0
                        count += 1
                elif x == 99:
                    if ladder[y+L[0]][x+L[1]] == 1:
                        y = y+L[0]
                        x = x+L[1]
                        d = -1
                        count += 1
                    elif ladder[y+D[0]][x+D[1]] == 1:
                        y = y + D[0]
                        x = x + D[1]
                        d = 0
                        count += 1
                else:
                    if d == 1:
                        if ladder[y+R[0]][x+R[1]] == 1:
                            y = y+R[0]
                            x = x+R[1]
                            d = 1
                            count += 1
                        elif ladder[y+D[0]][x+D[1]] == 1:
                            y = y + D[0]
                            x = x + D[1]
                            d = 0
                            count += 1
                    elif d == -1:
                        if ladder[y+L[0]][x+L[1]] == 1:
                            y = y+L[0]
                            x = x+L[1]
                            d = -1
                            count += 1
                        elif ladder[y+D[0]][x+D[1]] == 1:
                            y = y + D[0]
                            x = x + D[1]
                            d = 0
                            count += 1
                    elif d == 0:
                        if ladder[y+R[0]][x+R[1]] == 1:
                            y = y+R[0]
                            x = x+R[1]
                            d = 1
                            count += 1
                        elif ladder[y + L[0]][x + L[1]] == 1:
                            y = y + L[0]
                            x = x + L[1]
                            d = -1
                            count += 1
                        elif ladder[y+D[0]][x+D[1]] == 1:
                            y = y + D[0]
                            x = x + D[1]
                            d = 0
                            count += 1
        elif ladder[0][i] == 0:
            continue

        dic[i] = count

    # print(dic)
    # print(min(dic.values()))
    bank = []
    for ky, val in dic.items():
        if val == min(dic.values()):
            bank.append(ky)

    bank.sort()
    # print(bank)

    print('#{} {}'.format(tc+1, bank[-1]))