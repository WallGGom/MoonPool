import sys
sys.stdin = open('추억의 2048게임.txt', 'r')

# 왼쪽으로 밀어
def push_left(N, bank):
    for y in range(N):
        t = True
        while t:
            for x in range(1, N):
                if bank[y][x - 1] == 0:
                    bank[y][x - 1], bank[y][x] = bank[y][x], bank[y][x - 1]
            count = 0
            for x in range(N):
                if bank[y][x] == 0:
                    count += 1
            zero = 0
            for x in range(N-count,N):
                if bank[y][x] == 0:
                    zero += 1
                    if zero == count:
                        t = False
            if count == 0:
                t = False

    # print(bank)
    # 합체
    for y in range(N):
        for x in range(1,N):
            if bank[y][x-1] == bank[y][x]:
                bank[y][x-1] = bank[y][x]*2
                for pull in range(x, N):
                    if pull == (N - 1):
                        bank[y][pull] = 0
                    else:
                        bank[y][pull] = bank[y][pull + 1]
    # print(bank)
    return bank

# 오른쪽으로 밀어
def push_right(N, bank):
    for y in range(N):
        t = True
        while t:
            for x in range(N-1, 0,-1):
                if bank[y][x] == 0:
                    bank[y][x - 1], bank[y][x] = bank[y][x], bank[y][x - 1]
            count = 0
            for x in range(N):
                if bank[y][x] == 0:
                    count += 1
            zero = 0
            for x in range(count):
                if bank[y][x] == 0:
                    zero += 1
                    if zero == count:
                        t = False
            if count == 0:
                t = False


    # print(bank)
    # 합체
    for y in range(N):
        for x in range(N-1, 0,-1):
            if bank[y][x-1] == bank[y][x]:
                bank[y][x] = bank[y][x-1]*2
                for pull in range(x-1,-1,-1):
                    if pull == 0:
                        bank[y][pull] = 0
                    else:
                        bank[y][pull] = bank[y][pull - 1]
    # print(bank)
    return bank

# 아래 밀어
def push_down(N, bank):
    for x in range(N):
        t = True
        while t:
            for y in range(N - 1, 0, -1):
                if bank[y][x] == 0:
                    bank[y - 1][x], bank[y][x] = bank[y][x], bank[y - 1][x]
            count = 0
            for y in range(N):
                if bank[y][x] == 0:
                    count += 1
            zero = 0
            for y in range(count):
                if bank[y][x] == 0:
                    zero += 1
                    if zero == count:
                        t = False
            if count == 0:
                t = False

    # print(bank)
    # 합체
    for x in range(N):
        for y in range(N - 1, 0, -1):
            if bank[y - 1][x] == bank[y][x]:
                bank[y][x] = bank[y - 1][x] * 2
                for pull in range(y - 1, -1, -1):
                    if pull == 0:
                        bank[pull][x] = 0
                    else:
                        bank[pull][x] = bank[pull - 1][x]
    # print(bank)
    return bank

#위로 밀어
def push_up(N, bank):
    for x in range(N):
        t = True
        while t:
            for y in range(1, N):
                if bank[y - 1][x] == 0:
                    bank[y - 1][x], bank[y][x] = bank[y][x], bank[y - 1][x]
            count = 0
            for y in range(N):
                if bank[y][x] == 0:
                    count += 1
            zero = 0
            for y in range(N-count, N):
                if bank[y][x] == 0:
                    zero += 1
                    if zero == count:
                        t = False
            if count == 0:
                t = False

    # print(bank)
    # 합체
    for x in range(N):
        for y in range(1,N):
            if bank[y-1][x] == bank[y][x]:
                bank[y-1][x] = bank[y][x]*2
                for pull in range(y, N):
                    if pull == (N - 1):
                        bank[pull][x] = 0
                    else:
                        bank[pull][x] = bank[pull + 1][x]
    # print(bank)
    return bank

T = int(input())

for tc in range(T):
    n, O = map(str, input().split())
    N = int(n)

    bank = []
    for i in range(N):
        bank.append(list(map(int, input().split())))
    # print(bank)

    if O == 'up':
        ans = push_up(N, bank)
    elif O == 'down':
        ans = push_down(N, bank)
    elif O == 'right':
        ans = push_right(N, bank)
    elif O == 'left':
        ans = push_left(N, bank)
    print('#{}'.format(tc+1))
    for i in ans:
        res = ''
        for pic in i:
            res += str(pic) + ' '
        print(res)