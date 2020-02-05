import sys
sys.stdin = open('영준이의 카드 카운팅.txt', 'r')

T = int(input())


for tc in range(T):
    S = [0]*13
    D = [0]*13
    H = [0]*13
    C = [0]*13
    card = input()
    # print(card)
    # print(len(card))
    t = True
    for x in range(len(card)//3):
        typ = card[0+(3*x):1+(3*x)]
        num = card[1+(3*x):3+(3*x)]
        # print(type(typ))
        # print(num)
        if typ == 'S':
            S[int(num)] += 1
        elif typ == 'D':
            D[int(num)] += 1
        elif typ == 'H':
            H[int(num)] += 1
        elif typ == 'C':
            C[int(num)] += 1

    if 2 in S:
        t = False
    elif 2 in D:
        t = False
    elif 2 in H:
        t = False
    elif 2 in C:
        t = False

    dic = {'S': 13, 'D': 13, 'H': 13, 'C': 13}
    if t:
        dic['S'] -= S.count(1)
        dic['D'] -= D.count(1)
        dic['H'] -= H.count(1)
        dic['C'] -= C.count(1)
        res = '{} {} {} {}'.format(dic['S'], dic['D'], dic['H'], dic['C'])

    else:
        res = 'ERROR'

    print('#{} {}'.format(tc+1, res))









