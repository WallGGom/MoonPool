import sys
sys.stdin = open('1일차 - Flatten.txt', 'r')

def MX(a):
    zero = 0
    for i in a:
        if i > zero:
            zero = i
    return zero

def mn(b):
    zero = MX(b)
    for i in b:
        if i < zero:
            zero = i
    return zero

T = 10

for tc in range(T):
    num = int(input())
    data = list(map(int, input().split())) #공백으로 구분해서 int로 받아서 list를 만든다.
    # print(data)

    for i in range(num):
        data[data.index(MX(data))] -= 1
        data[data.index(mn(data))] += 1
    print('#{} {}'.format(tc+1, MX(data)-mn(data)))








