import sys
sys.stdin = open('삼성시의 버스 노선.txt', 'r')


T = int(input())

for tc in range(T):
    N = int(input())
    Bus_stop = [0] * 5000
    for case in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            Bus_stop[i-1] += 1
    # print(Bus_stop)


    P = int(input())
    stop = []
    for _ in range(P):
        C = int(input())
        stop.append(C)

    res = ""
    for pic in stop:
        res += str(Bus_stop[pic-1]) + ' '

    print('#{} {}'.format(tc+1, res))

'''

T = int(input())
for t in range(1, T + 1):
    lines = int(input())

    line_info = [0] * 5000

    for l in range(lines):
        A, B = map(int, input().split())
        for i in range(A - 1, B):
            line_info[i] += 1
    print(line_info)

    stops = int(input())
    stop_info = []
    for s in range(stops):
        stop_info.append(int(input()))
    print(stop_info)

    result = []

    for stop in stop_info:
        result.append(line_info[stop - 1])
    print(result)

    print('#{}'.format(t), *result)

'''