import sys
sys.stdin = open('재미있는 오셀로 게.txt', 'r')

T = int(input())

def sear(bank):
    for j in bank:
        if y - j[1] == 0:
            for k in range(1, abs(j[0] - x)):
                if plane[y][x + k] == abs(c - 3):
                    plane[y][x + k] = c
                elif plane[y][x - k] == abs(c - 3):
                    plane[y][x - k] = c
        elif x - j[0] == 0:
            for k in range(1, abs(j[1] - y)):
                if plane[y + k][x] == abs(c - 3):
                    plane[y + k][x] = c
                elif plane[y - k][x] == abs(c - 3):
                    plane[y - k][x] = c
        elif j[0] - x > 0 and j[1] - y < 0:
            for k in range(1, abs(j[0] - x)):
                if plane[y - k][x + k] == abs(c - 3):
                    plane[y - k][x + k] = c
        elif j[0] - x > 0 and j[1] - y > 0:
            for k in range(1, abs(j[0] - x)):
                if plane[y + k][x + k] == abs(c - 3):
                    plane[y + k][x + k] = c
        elif j[0] - x < 0 and j[1] - y > 0:
            for k in range(1, abs(j[0] - x)):
                if plane[y + k][x - k] == abs(c - 3):
                    plane[y + k][x - k] = c
        elif j[0] - x < 0 and j[1] - y < 0:
            for k in range(1, abs(j[0] - x)):
                if plane[y - k][x - k] == abs(c - 3):
                    plane[y - k][x - k] = c
    return

for tc in range(T):
    N, M = map(int, input().split())
    plane = [[0]*(3*N-2) for i in range(3*N-2)]
    # print(plane)
    for y in range((3*N-2)//2-1,(3*N-2)//2+1):
        for x in range((3*N-2)//2-1,(3*N-2)//2+1):
            if y == x:
                plane[y][x] = 2
            else:
                plane[y][x] = 1
    # print(plane)

    idx = [-1,0,1,0,-1,1,1,-1]
    idy = [0,-1,0,1,-1,-1,1,1]

    for _ in range(M):
        a, b, c = map(int, input().split())
        x = a + (N-2)
        y = b + (N-2)
        count = 0
        for search in range(8):
            for i in range(2, N):
                if plane[y+(idy[search]*(i-1))][x+(idx[search]*(i-1))] == abs(c-3) and plane[y+(idy[search]*i)][x+(idx[search]*i)] == c:
                    plane[y][x] = c
                    count += 1
                    break
        if count == 0:
            break
        lis = []
        for search in range(8):
            for i in range(2, N):
                if plane[y + idy[search]*i][x + idx[search]*i] == c:
                    sub = [x + idx[search]*i, y + idy[search]*i]
                    lis.append(sub)
                    break
        sear(lis)
        # lis = []
        # for y in range(N-1,N+(N-1)):
        #     for x in range(N-1,N+(N-1)):
        #         for search in range(8):
        #             for i in range(2, N):
        #                 if plane[y][x] == 1 and plane[y + idy[search] * i][x + idx[search] * i] == 1:
        #                     sub = [x + idx[search] * i, y + idy[search] * i]
        #                     lis.append(sub)
        #                     c = 1
        #                     break
        #                 elif plane[y][x] == 2 and plane[y + idy[search] * i][x + idx[search] * i] == 2:
        #                     sub = [x + idx[search] * i, y + idy[search] * i]
        #                     lis.append(sub)
        #                     c = 2
        #                     break
        #                 sear(lis)
        #                 lis = []


    # print(plane)

    num1 = 0
    num2 = 0
    for l in plane:
        num1 += l.count(1)
        num2 += l.count(2)

    # print(num1)
    # print(num2)
    print('#{} {} {}'.format(tc+1, num1, num2))










        # for search in range(8):
        #     if plane[y][x] == 1 and plane[y+idy[search]][x+idx[search]] == 2 and plane[y+(idy[search]*2)][x+(idx[search]*2)] == 1:
        #         plane[y + idy[search]][x + idx[search]] = 1
        #         X = x + idx[search]
        #         Y = y + idy[search]
        #         for search in range(8):
        #             if plane[Y][X] == 1 and plane[Y + idy[search]][X + idx[search]] == 2 and \
        #                     plane[Y + (idy[search] * 2)][X + (idx[search] * 2)] == 1:
        #                 plane[Y + idy[search]][X + idx[search]] = 1
        #
        #
        #     elif plane[y][x] == 2 and plane[y+idy[search]][x+idx[search]] == 1 and plane[y+(idy[search]*2)][x+(idx[search]*2)] == 2:
        #         plane[y + idy[search]][x + idx[search]] = 2
        #         X = x + idx[search]
        #         Y = y + idy[search]
        #         for search in range(8):
        #             if plane[Y][X] == 2 and plane[Y + idy[search]][X + idx[search]] == 1 and \
        #                     plane[Y + (idy[search] * 2)][X + (idx[search] * 2)] == 2:
        #                 plane[Y + idy[search]][X + idx[search]] = 2

    # print(plane)

        # if 0 <= y < (N//2) and 0 <= x < (N//2):
        #     for search in range(3,8):
        #         if c == 1 and plane[y+idy[search]][x+idx[search]] == 2 and plane[y+(idy[search]*2)][x+(idx[search]*2)] == 1:
        #             plane[y + idy[search]][x + idx[search]] = 1
        #         elif c == 2 and plane[y+idy[search]][x+idx[search]] == 1 and plane[y+(idy[search]*2)][x+(idx[search]*2)] == 2:
        #             plane[y + idy[search]][x + idx[search]] = 2
        # elif 0 <= y < (N//2) and (N//2) <= x < N:
        #     for search in range(1,-4,-1):
        #         if c == 1 and plane[y+idy[search]][x+idx[search]] == 2 and plane[y+(idy[search]*2)][x+(idx[search]*2)] == 1:
        #             plane[y + idy[search]][x + idx[search]] = 1
        #         elif c == 2 and plane[y+idy[search]][x+idx[search]] == 1 and plane[y+(idy[search]*2)][x+(idx[search]*2)] == 2:
        #             plane[y + idy[search]][x + idx[search]] = 2
        # elif (N//2) <= y < N and 0 <= x < (N//2):
        #     for search in range(1,6):
        #         if c == 1 and plane[y+idy[search]][x+idx[search]] == 2 and plane[y+(idy[search]*2)][x+(idx[search]*2)] == 1:
        #             plane[y + idy[search]][x + idx[search]] = 1
        #         elif c == 2 and plane[y+idy[search]][x+idx[search]] == 1 and plane[y+(idy[search]*2)][x+(idx[search]*2)] == 2:
        #             plane[y + idy[search]][x + idx[search]] = 2
        # elif (N//2) <= y < N and (N//2) <= x < N:
        #     for search in range(1,6):
        #         if c == 1 and plane[y+idy[search]][x+idx[search]] == 2 and plane[y+(idy[search]*2)][x+(idx[search]*2)] == 1:
        #             plane[y + idy[search]][x + idx[search]] = 1
        #         elif c == 2 and plane[y+idy[search]][x+idx[search]] == 1 and plane[y+(idy[search]*2)][x+(idx[search]*2)] == 2:
        #             plane[y + idy[search]][x + idx[search]] = 2


    # count1 = 0
    # count2 = 0

# for seq in range(N):
#     for y in range(2, 2 + N):
#         for x in range(2, 2 + N):