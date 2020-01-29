import sys
sys.stdin = open('홀수만 더하기_input.txt', 'r')

N = int(input())

for tc in range(N):
    data = list(map(int, input().split())) #공백으로 구분해서 int로 받아서 list를 만든다.
    sum = 0
    # print(data)
    for i in range(10):
        if (data[i] % 2):
            sum += data[i]
    print('#{} {}'.format(tc, sum))
    sum = 0




