import sys
sys.stdin = open('5일차 - GNS.txt','r')

T = int(input())
for _ in range(T):
    tc, L = map(str, input().split())
    total = list(map(str, input().split()))
    # print(total)

    bank = [0]*10
    for i in total:
        if i == "ZRO":
            bank[0] += 1
        elif i == "ONE":
            bank[1] += 1
        elif i == "TWO":
            bank[2] += 1
        elif i == "THR":
            bank[3] += 1
        elif i == "FOR":
            bank[4] += 1
        elif i == "FIV":
            bank[5] += 1
        elif i == "SIX":
            bank[6] += 1
        elif i == "SVN":
            bank[7] += 1
        elif i == "EGT":
            bank[8] += 1
        elif i == "NIN":
            bank[9] += 1
    # print(bank)

    res = ''
    for idx, val in enumerate(bank):
        if idx == 0:
            res += ('ZRO ' * val)
        elif idx == 1:
            res += ('ONE ' * val)
        elif idx == 2:
            res += ('TWO ' * val)
        elif idx == 3:
            res += ('THR ' * val)
        elif idx == 4:
            res += ('FOR ' * val)
        elif idx == 5:
            res += ('FIV ' * val)
        elif idx == 6:
            res += ('SIX ' * val)
        elif idx == 7:
            res += ('SVN ' * val)
        elif idx == 8:
            res += ('EGT ' * val)
        elif idx == 9:
            res += ('NIN ' * val)

    print(tc)
    print(res)

