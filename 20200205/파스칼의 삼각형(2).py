import sys
sys.stdin = open('파스칼의 삼각형.txt', 'r')

T = int(input())

for tc in range(T):
    num = int(input())
    bank = [[0]*num for _ in range(num)]
    # print(bank)

    for y in range(num):
        for x in range(num):
            if x == y:
                bank[y][x] = 1
            elif x == 0:
                bank[y][0] = 1
            elif y >= 2 and x >= 1:
                bank[y][x] = bank[y-1][x] + bank[y-1][x-1]
    # print(bank)

    res = ""
    for y in range(num):
        for x in range(num):
            if y > x:
                res += str(bank[y][x]) + ' '
            elif y == x:
                res += str(bank[y][x]) + '\n'

    print('#{}\n{}'.format(tc+1, res[:len(res)-1]))

