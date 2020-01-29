import sys
sys.stdin = open('2일차 - 최대 상금.txt', 'r')

T = int(input())

for tc in range(T):
    data, N = map(int, input().split()) #공백으로 구분해서 int로 받아서 list를 만든다.
    count = 0

    while count < N:
        for i in range(len(data)):
            if data[count] < data[i]:
                for k in range(len(data)):
                if data[i] == data[i+1]:
                    data[0], data[i + 1] == data[i + 1], data[0]
                if data[i] == data[i+2]:
                    data[0], data[i + 2] == data[i + 2], data[0]


                else:
                    data[0], data[i] == data[i], data[0]




