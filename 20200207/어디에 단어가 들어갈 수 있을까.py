import sys
sys.stdin = open('어디에 단어가 들어갈 수 있을까.txt', 'r')

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())

    plane = []
    for _ in range(N):
        plane.append(list(map(int, input().split())))

    print(plane)

    ans = 0
    for y in range(N):
        count = 0
        flag = 0
        for x in range(N):
            if plane[y][x] == 1:
                count += 1
                flag = 1
            elif flag == 1 and plane[y][x] == 0:
                if count == K:
                    ans += 1
                    count = 0
                else:
                    count = 0
        if count == K:
            ans += 1

    for x in range(N):
        count = 0
        flag = 0
        for y in range(N):
            if plane[y][x] == 1:
                count += 1
                flag = 1
            elif flag == 1 and plane[y][x] == 0:
                if count == K:
                    ans += 1
                    count = 0
                else:
                    count = 0
        if count == K:
            ans += 1

    print('#{} {}'.format(tc+1, ans))