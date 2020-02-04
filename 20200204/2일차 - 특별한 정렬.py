import sys
sys.stdin = open('2일차 - 특별한 정렬.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    num = list(map(int, input().split()))
    num.sort()
    # print(num)

    array = [0] * 10
    for i in range(0, 10, 2):
        array[i] = num[-((i//2)+1)]
    for j in range(1, 10, 2):
        array[j] = num[j//2]

    result = ''
    for k in range(10):
        result += str(array[k]) + " "

    print('#{} {}'.format(tc + 1, result))