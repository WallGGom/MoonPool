import sys
sys.stdin = open('파리 퇴치.txt', 'r')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    Array = []

    for i in range(N):
        Array.append(list(map(int, input().split())))
    # print(Array)

    idx = []
    idy = []

    for dx in range(M):
        for dy in range(M):
            idx.append(dx)
            idy.append(dy)
    # print(idx)
    # print(idy)

    result = []
    bank = []
    for y in range(N-M+1):
        for x in range(N-M+1):
            for d in range(len(idx)):
                bank.append(Array[y+idy[d]][x+idx[d]])
            result.append(sum(bank))
            bank = []
    print('#{} {}'.format(tc+1, max(result)))