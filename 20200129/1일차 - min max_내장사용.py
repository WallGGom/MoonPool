import sys
sys.stdin = open('1일차 - min max.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    data = list(map(int, input().split())) #공백으로 구분해서 int로 받아서 list를 만든다.
    for num in range(N):
        sub = max(data) - min(data)

    print('#{} {}'.format(tc+1, sub))