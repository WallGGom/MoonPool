import sys
sys.stdin = open('4일차 - 그래프 경로.txt', 'r')

def DFS(s):
    global res
    visited[s] = 1
    for n in range(1, V+1):
        if Map[s][n] and not visited[n]:
            if n == G:
                res = 1
                return
            DFS(n)

T = int(input())
for tc in range(T):
    res = 0
    V, E = map(int, input().split())
    Map = [[0]*(V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    for i in range(E):
        start, end = map(int, input().split())
        Map[start][end] = 1
    # print(Map)
    S, G = map(int, input().split())

    DFS(S) 

    print('#{} {}'.format(tc+1, res))





