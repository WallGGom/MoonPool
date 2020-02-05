import sys
sys.stdin = open('기차 사이의 파리.txt', 'r')


T = int(input())

for tc in range(T):
    D, A, B, F = map(int, input().split())

    time = D / (A + B)

    res = F * time

    print('#{} {:.6f}'.format(tc + 1, res))





