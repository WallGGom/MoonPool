import sys
sys.stdin = open('힙.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    order = []
    hip = []
    # count_1 = 0
    # count_2 = 0
    for i in range(N):
        order.append(list(map(int, input().split())))
    print('#{} '.format(tc+1), end='')
    for j in order:
        if j[0] == 1:
            hip.append(j[1])
            hip.sort()
            count_1 += 1
        elif j[0] == 2 and len(hip) > 0:
            print(hip.pop(), end=' ')
            count_2 += 1
        elif j[0] == 2 and len(hip) == 0:
            print('-1', end=' ')
            count_1 = 0
            count_2 = 0
    if count_1 < count_2:
        res = -1
    print()
