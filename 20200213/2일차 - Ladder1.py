import sys
sys.stdin = open('2일차 - Ladder1.txt', 'r')

T = 10

for tc in range(T):
    TC = input()
    ladder = [list(map(int,input().split())) for _ in range(100)]
    # print(ladder)

    for i in range(100):
        if ladder[99][i] == 2:
            start = i
            x = i
            y = 99
            count = 0
            d = 0
            while y > 0:
                if x == 0:
                    if d == -1:
                        y -= 1
                        d = 0
                    elif ladder[y][x+1]:
                        count += 1
                        x += 1
                        d = 1
                    elif ladder[y-1][x]:
                        y -= 1
                        d = 0
                elif x == 99:
                    if d == 1:
                        y -= 1
                        d = 0
                    elif ladder[y][x-1]:
                        count += 1
                        x -= 1
                        d = -1
                    elif ladder[y-1][x]:
                        y -= 1
                        d = 0
                else:
                    if d == 1:
                        if ladder[y][x+1]:
                            count += 1
                            x += 1
                            d = 1
                        elif ladder[y-1][x]:
                            y -= 1
                            d = 0
                    elif d == -1:
                        if ladder[y][x-1]:
                            count += 1
                            x -= 1
                            d = -1
                        elif ladder[y - 1][x]:
                            y -= 1
                            d = 0
                    elif d == 0:
                        if ladder[y][x+1]:
                            count += 1
                            x += 1
                            d = 1
                        elif ladder[y][x-1]:
                            count += 1
                            x -= 1
                            d = -1
                        elif ladder[y-1][x]:
                            y -= 1
                            d = 0
            if ladder[0][x] == 1:
                print('#{} {}'.format(tc+1, x))
                break