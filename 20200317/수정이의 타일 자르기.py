import sys
sys.stdin = open('수정이의 타일 자르기.txt','r')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    jumun = list(map(int, input().split()))
    jumun.sort()
    # print(jumun)
    tile = [[M, M]]
    cnt = 1

    while jumun:
        temp = jumun.pop()
        side = 2 ** temp
        t = True
        for ind, i in enumerate(tile):
            if i[0] - side >= 0 and i[1] - side >= 0:
                t = False
                y, x = tile.pop(ind)
                if y - side >= 1 and x - side >= 1:
                    tile.append([side,x-side])
                    tile.append([y-side,x-side])
                    tile.append([y-side,side])
                elif y - side == 0 and x - side >= 1:
                    tile.append([side,x-side])
                elif y - side >= 1 and x - side == 0:
                    tile.append([y-side,side])
                break
        if t:
            jumun.append(temp)
            tile.append([M,M])
            cnt += 1

    print(f'#{tc+1} {cnt}')