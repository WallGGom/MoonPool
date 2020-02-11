import sys
sys.stdin = open('최대 성적표 만들기.txt', 'r')

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort()

    MX = sum(score[-K:])
    print('#{} {}'.format(tc+1, MX))





