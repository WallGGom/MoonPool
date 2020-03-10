import sys
sys.stdin = open('창용 마을 무리의 개수.txt', 'r')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    chingu = [[0] * (N+1) for _ in range(N+1)]
    # print(chingu)
    visited = [0] * (N+1)
    for i in range(M):
        p1, p2 = map(int, input().split())
        chingu[p1][p2] = chingu[p2][p1] = 1
    # print(chingu)

    temp = []
    cnt = 0
    for i in range(1,N+1):
        if visited[i] == 0:
            temp.append(i)
            nxt = i
            visited[i] = 1
            while temp:
                for j in range(1, N+1):
                    if chingu[nxt][j] == 1 and visited[j] == 0:
                        temp.append(j)
                        visited[j] = 1
                else:
                    nxt = temp.pop()
            cnt += 1
    print(f'#{tc+1} {cnt}')


