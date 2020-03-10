import sys
sys.stdin = open('최장 경로2.txt','r')
"""
M이 0 이면 1출력
M이 0이 아니면 DFS로 경로 탐색하여 최다 노드가 나오는 경로의 최대값 출력
"""
T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    matrix = [[0] * (N+1) for _ in range(N+1)]
    for m in range(M):
        x, y = map(int,input().split())
        matrix[x][y] = matrix[y][x] = 1
    print(matrix)
    result = list()
    if M:
        for i in range(1,N+1):
            visited = [0] * (N + 1)
            now = list()
            now.append(i)
            visited[i] = 1
            while len(now):
                n = now.pop(-1)
                for j in range(1,N+1):
                    if matrix[n][j] == 1 and visited[j] != 1:
                        visited[j] = 1
                        now.append(j)

            result.append(sum(visited))
        print('#{} {}'.format(tc+1,max(result)))
    else:
        print('#{} {}'.format(tc+1,1))