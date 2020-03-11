import sys
sys.stdin = open('최솟값으로 이동하기.txt', 'r')

T = int(input())
for tc in range(T):
    W, H, N = map(int, input().split())
    start = list(map(int, input().split()))
    cnt = 0
    for _ in range(N-1):
        nxt = list(map(int, input().split()))
        d_x, d_y = nxt[0] - start[0], nxt[1] - start[1]
        if d_x > 0 and d_y > 0:
            while d_x > 0 and d_y > 0:
                d_x -= 1
                d_y -= 1
                cnt += 1
            cnt += abs(d_x) + abs(d_y)
        elif d_x < 0 and d_y < 0:
            while d_x < 0 and d_y < 0:
                d_x += 1
                d_y += 1
                cnt += 1
            cnt += abs(d_x) + abs(d_y)
        else:
            cnt += abs(d_x) + abs(d_y)
        start = nxt
    print(f'#{tc+1} {cnt}')