import sys
sys.stdin = open('1일차 - Flatten.txt', 'r')
T = 10

for tc in range(T):
    num = int(input())
    data = list(map(int, input().split()))  # 공백으로 구분해서 int로 받아서 list를 만든다.
    # print(data)

    for i in range(num):
        data[data.index(max(data))] -= 1
        data[data.index(min(data))] += 1
    print('#{} {}'.format(tc + 1, max(data) - min(data)))