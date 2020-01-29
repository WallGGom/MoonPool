import sys
sys.stdin = open('평균값 구하기.txt', 'r')

T = int(input())

for tc in range(T):
    data = list(map(int, input().split())) #공백으로 구분해서 int로 받아서 list를 만든다.

    a = sum(data) / len(data)
    b = round(a)
    print('#{} {}'.format(tc+1, b))