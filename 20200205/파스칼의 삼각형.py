import sys
sys.stdin = open('파스칼의 삼각형.txt', 'r')

T = int(input())

for tc in range(T):
    num = int(input())

    if num == 1:
        res = ''

    elif num == 2:
        res = '\n1 1\n'

    else:
        lst = [[1,1]]
        for y in range(num-2):
            res = []
            res.append(1)
            for x in range(len(lst[y])-1):
                res.append(lst[y][x] + lst[y][x + 1])
            res.append(1)
            lst.append(res)
        a = "\n"
        for Y in range(len(lst)):
            for X in range(len(lst[Y])):
                a += str(lst[Y][X]) + " "
            a += '\n'
        res = a

    print('#{}\n1{}'.format(tc+1, res[:len(res)-1]))






    # print(lst)

