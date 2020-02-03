import sys
sys.stdin = open('2일차 - Sum.txt', 'r')

T = 10

for tc in range(T):
    TC = input()
    bank = []
    datalist = []


    for k in range(100):
        datalist.append(list(map(int, input().split()))) #공백으로 구분해서 int로 받아서 list를 만든다.
        # print(datalist)
        # bank.append(datalist[i * 100:(i+1) * 100])
        # print(bank)

    # for y in range(100):
    #     for x in range(100):
    #         bank[y][x] = datalist[x + 10*y]
    storage = datalist
    for y in range(100):
        bank.append(sum(datalist[y]))

    for i in range(100):
        for j in range(100):
            if i < j :
                storage[i][j], storage[j][i] = storage[j][i], storage[i][j]

    for x in range(100):
        bank.append(sum(datalist[x]))

    ldru = []
    lurd = []
    for l in range(100):
        for p in range(100):
            if l == p:
                lurd.append(datalist[l][p])
            elif l == (99 - p):
                ldru.append(datalist[l][99 - p])

    DU = sum(ldru)
    UD = sum(lurd)

    bank.append(DU)
    bank.append(UD)

    print('#{} {}'.format(tc+1,max(bank)))









