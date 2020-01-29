import sys
sys.stdin = open('큰 놈, 작은 놈, 같은 놈.txt', 'r')

T = int(input())

for tc in range(T):
    data = list(map(int, input().split())) #공백으로 구분해서 int로 받아서 list를 만든다.
    if data[0] > data[1]:
        print('#{} >'.format(tc+1))
    elif data[0] < data[1]:
        print('#{} <'.format(tc+1))
    elif data[0] == data[1]:
        print('#{} ='.format(tc+1))
