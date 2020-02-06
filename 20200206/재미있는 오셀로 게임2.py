import sys
sys.stdin = open('재미있는 오셀로 게임.txt', 'r')

T = int(input())
Direction = []
for i in range(-1,2):
    for j in range(-1,2):
        if not i == 0 or not j == 0:
            Direction.append([i, j])

# print(Direction)

for tc in range(T):
    N, M = map(int, input().split())
    plane = [[0]*N for i in range(N)]
    # print(plane)
    h = N//2
    plane[h][h] = 2
    plane[h-1][h-1] = 2
    plane[h][h-1] = 1
    plane[h-1][h] = 1
    # print(plane)

    for _ in range(M):
        a, b, c = map(int, input().split())
        # print(a, b, c)
        x = a - 1
        y = b - 1
        plane[y][x] = c
        for idy, idx in Direction:
            for step in range(1, N):
                compare_y = y + idy*step
                compare_x = x + idx*step
                if 0 <= compare_y < N and 0 <= compare_x < N:
                    if plane[compare_y][compare_x] == 0:
                        break
                    elif plane[compare_y][compare_x] == c:
                        for ch in range(1, step):
                            change_y = y + idy*ch
                            change_x = x + idx*ch
                            plane[change_y][change_x] = c
                else:
                    break
    count1 = 0
    count2 = 0
    for i in plane:
        count1 += i.count(1)
        count2 += i.count(2)

    print('#{} {} {}'.format(tc+1, count1, count2))