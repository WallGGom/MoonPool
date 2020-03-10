import sys
sys.stdin = open('4일차 - 하나로.txt', 'r')


T = int(input())
for tc in range(T):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    route = [[0]*N for _ in range(N)]
    print(X)
    print(Y)

    dis = []
    for i in range(N-1):
        for j in range(i+1,N):
            dis_sq = abs(X[i] - X[j])**2 + abs(Y[i] - Y[j])**2
            route[i][j] = route[j][i] = dis_sq
            dis.append([dis_sq, i, j])
    print(dis)
    dis.sort()
    print(dis)