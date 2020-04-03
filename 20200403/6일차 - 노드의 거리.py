import sys
sys.stdin = open('6일차 - 노드의 거리.txt','r')

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    Table = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        Table[n1][n2] = Table[n2][n1] = 1
    S, G = map(int, input().split())
    # print(Table)
    # print(S,G)
    Q = []
    visited = [0]*(V+1)
    for j in range(V+1):
        if Table[S][j] == 1:
            visited[j] = 1
            Q.append((j,1))
    # print(Q)
    ans = 0
    while Q:
        temp = Q.pop(0)
        if temp[0] == G:
            ans = temp[1]
            break
        for k in range(V+1):
            if visited[k] == 0 and Table[temp[0]][k] == 1:
                visited[k] = 1
                Q.append((k,temp[1]+1))
    print(f'#{tc+1} {ans}')