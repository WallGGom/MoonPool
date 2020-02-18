import sys

sys.stdin = open('array_sum.txt', 'r')

T = int(input())


def result(n, currentsum):
    global minimum
    if currentsum < minimum:
        minimum = currentsum


def perm(n, k, currentsum):
    if currentsum >= minimum:
        return
    if k == n:
        result(n, currentsum)
    else:
        for i in range(k, n):
            idx[k], idx[i] = idx[i], idx[k]
            perm(n, k + 1, currentsum + array[k][idx[k]])
            idx[k], idx[i] = idx[i], idx[k]


for tc in range(T):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]

    idx = []
    for i in range(N):
        idx.append(i)

    minimum = 0xffffffff

    perm(N, 0, 0)

    print(f'#{tc+1} {minimum}')