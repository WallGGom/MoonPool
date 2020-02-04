import sys
sys.stdin = open('색칠하기.txt', 'r')

T = int(input())

for tc in range(T):
    n = int(input())
    Array = []
    for i in range(n):
        Array.append(list(map(int, input().split())))
    # print(Array)

    white = [[0]*10 for _ in range(10)]

    # print(white)

    for pong in range(len(Array)):
        if Array[pong][4] == 1:
            for y in range(Array[pong][1], Array[pong][3]+1):
                for x in range(Array[pong][0], Array[pong][2]+1):
                    white[y][x] += 1
        if Array[pong][4] == 2:
            for y in range(Array[pong][1], Array[pong][3]+1):
                for x in range(Array[pong][0], Array[pong][2]+1):
                    white[y][x] += 2
    # print(white)
    result = 0
    for k in range(10):
        result += white[k].count(3)
        result += white[k].count(4)
        result += white[k].count(5)

    print('#{} {}'.format(tc+1, result))






