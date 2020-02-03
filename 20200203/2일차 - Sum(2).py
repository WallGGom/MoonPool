import sys
sys.stdin = open('2일차 - Sum.txt', 'r')

for i in range(10):
    plot = []
    c = input()
    for i in range(100):
        numbers = list(map(int, input().split()))
        sum_num = sum(numbers)
        plot.append(numbers)

    horiz_nums = max([sum(x) for x in plot])
    verti_nums = max([sum(x) for x in list(zip(*plot))])
    diagonal_sum1 = sum([plot[i][i] for i in range(0, 100)])
    diagonal_sum2 = sum([plot[i][99 - i] for i in range(0, 100)])

    print('#{} {}'.format(c, max(horiz_nums, verti_nums, diagonal_sum1, diagonal_sum2)))