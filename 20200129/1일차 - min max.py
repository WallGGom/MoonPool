import sys
sys.stdin = open('1일차 - min max.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    data = list(map(int, input().split())) #공백으로 구분해서 int로 받아서 list를 만든다.
    for num in range(N):
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if data[i] > data[j]:
                    data[i], data[j] = data[j], data[i]
        sub = data[len(data)-1] - data[0]

    print('#{} {}'.format(tc+1, sub))