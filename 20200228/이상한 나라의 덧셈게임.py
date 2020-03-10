import sys
sys.stdin = open('이상한 나라의 덧셈게임.txt','r')

T = int(input())
for tc in range(T):
    N = str(input())
    num = []
    for i in N:
        num.append(int(i))
    # print(num)
    L = len(num)
    count = 0
    while L > 1:
        bank = []
        for i in range(L-1):
            bank.append(num[i]+num[i+1])
        # print(bank)
        if bank:
            pick = bank.index(max(bank))
            a = str(max(bank))
            a_rev = a[::-1]
            for step in range(2):
                a = num.pop(pick)
            # print(num)
            for i in a_rev:
                num.insert(pick, int(i))
            # print(num)
            count += 1
            L = len(num)
    # print(count)

    if count % 2:
        res = 'A'
    else:
        res = 'B'

    print('#{} {}'.format(tc+1, res))