import sys
sys.stdin = open('최대수 구하기.txt', 'r')

T = int(input())

for tc in range(T):
    data = list(map(int, input().split())) #공백으로 구분해서 int로 받아서 list를 만든다.
    MX = 0

    for i in data:
        if i > MX:
            MX = i
    print('#{} {}'.format(tc+1,MX))


