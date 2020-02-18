import sys
sys.stdin = open('5일차 - 배열 최소 합.txt', 'r')

def hap(y):
    global result
    if y == N:
        stack.append(result)

    for x in range(N):
        if not visited[x]:
            visited[x] = 1
            result += Table[y][x]
            hap(y+1)
            visited[x] = 0
            result -= Table[y][x]


T = int(input())
for tc in range(T):
    N = int(input())
    Table = [[int(_) for _ in input().split()] for _ in range(N)]
    # print(Table)

    stack = []
    result = 0
    visited = [0]*N
    hap(0)
    print(stack)
    # print('#{} {}'.format(tc+1, min(stack)))

