import sys
sys.stdin = open('수의 새로운 연산.txt', 'r')

# N = 265
# plane = [[0]*N for _ in range(N)]
# stack = 0
# stair = 1
# count = 0
# for y in range(N):
#     step = 2 + count
#     for x in range(N):
#         if x == 0 and y == 0:
#             plane[0][0] = 1
#         elif x == 0 and y > 0:
#             plane[y][x] = plane[y-1][x] + stair
#             stair += 1
#         else:
#             plane[y][x] = plane[y][x-1] + step
#             step += 1
#     count += 1
# # print(plane)


def axis(p):
    N = 300
    step = 2
    count = 0
    bank = []
    P = True
    for _ in range(N):
        if _ == 0:
            ans = 1
            count += 1
            if p == 1 and P:
                x = 1
                y = 1
                bank.append([x, y])
                P = False
        else:
            ans = ans + step
            if ans >= p and P:
                x = count - (ans - p) + 1
                y = ans - p + 1
                if y >= 0 and x >= 0:
                    bank.append([x, y])
                    P = False
            step += 1
            count += 1
    return bank

def val(x, y):
    N = 300
    step = 2
    for _ in range(N):
        if _ == 0:
            ans = 1
            count = 1
        else:
            ans = ans + step
            step += 1
            count += 1
            if count == x:
                stair = x
                for st in range(y-1):
                    ans += stair + st
                break
    return ans


T = int(input())
for tc in range(T):
    p, q = list(map(int, input().split()))
    # print(tc, p, q)
    # print(axis(p))
    # print(axis(q))

    X = axis(p)[0][0] + axis(q)[0][0]
    Y = axis(p)[0][1] + axis(q)[0][1]

    # print(X, Y)
    print('#{} {}'.format(tc+1,val(X, Y)))













# T = int(input())
# for tc in range(T):
#     p, q = map(int, input().split())
#     # print(p, q)
#
#     # P = []
#     # Q = []
#     for y in range(N):
#         for x in range(N):
#             if p == q and plane[y][x] == p:
#                 P = [x+1, y+1]
#                 Q = [x+1, y+1]
#             elif plane[y][x] == p:
#                 P = [x+1, y+1]
#             elif plane[y][x] == q:
#                 Q = [x+1, y+1]
#     # print(P)
#     # print(Q)
#     ans = plane[P[1]+Q[1]-1][P[0]+Q[0]-1]
#     print('#{} {}'.format(tc+1, ans))