import sys
sys.stdin = open('영준이와 신비한 뿔의 숲.txt', 'r')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    x = N - M
    y = M - x
    print('#{} {} {}'.format(tc+1, y, x))