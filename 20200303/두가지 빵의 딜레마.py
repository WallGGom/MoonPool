import sys
sys.stdin = open('두가지 빵의 딜레마.txt', 'r')

T = int(input())
for tc in range(T):
    A, B, C = map(int, input().split())

    less = min(A, B)
    res = C // less
    print(f'#{tc+1} {res}')