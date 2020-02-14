import sys
sys.stdin = open('10일차 - 작업순서.txt', 'r')

T = 10
for tc in range(T):
    V, E = map(int, input().split())
    gan = list(map(int, input().split()))
    Table = [[0] * (V + 1) for _ in range(V + 1)]
    visited = []

    for i in range(0, len(gan), 2):
        Table[gan[i+1]][gan[i]] = 1
    # print(Table)

    while len(visited) != V:
        for i in range(1, V+1):
            # b = sum(Table[i])
            if sum(Table[i]) == 0: # i로 가는 간선 없음, 시작점이 될꺼야
                if str(i) not in visited:
                    visited.append(str(i))
                for j in range(1, V+1):
                    if Table[j][i] == 1: # i에서 j로 들어가는 간선이 존재함
                        Table[j][i] = 0 # j로 들어가는 간선을 없앰
    print('#{} {}'.format(tc+1, ' '.join(visited)))