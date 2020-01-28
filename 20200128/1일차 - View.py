import sys
sys.stdin = open('1일차 - View_input.txt', 'r')

T = 10

for tc in range(T):
    N = int(input())
    data = list(map(int, input().split())) #공백으로 구분해서 int로 받아서 list를 만든다.
    count = 0
    # print(data)
    # print(max(data[3], data[4], data[5]))
    for i in range(2, N-2):
        if data[i] > max(data[i-2], data[i-1], data[i+1], data[i+2]):
            num = data[i] - max(data[i-2], data[i-1], data[i+1], data[i+2])
            count += num

    print('#{} {}'.format(tc+1, count))  #정답
