import sys
sys.stdin = open('나는 개구리로소이다.txt','r')

T = int(input())

for tc in range(T):

    word = list(input())
    print(word)
    # while t:
    bank = []
    res = ''
    count_A = 0
    for idx, w in enumerate(word):
        if w == 'c' and res == '':
            res += w
            bank.append(idx)
        if w == 'r' and res == 'c':
            res += w
            bank.append(idx)
        if w == 'o' and res == 'cr':
            res += w
            bank.append(idx)
        if w == 'a' and res == 'cro':
            res += w
            bank.append(idx)
        if w == 'k' and res == 'croa':
            res += w
            bank.append(idx)
    if len(bank) == 5:
        for i in range(bank[0], bank[-1]):
            if word[i] == 'c':
                count_A += 1
    print(count_A)

    t = True
    while t:
        bank = []
        res = ''
        count = 0
        for idx, w in enumerate(word):
            if w == 'c' and res == '':
                res += w
                bank.append(idx)
            if w == 'r' and res == 'c':
                res += w
                bank.append(idx)
            if w == 'o' and res == 'cr':
                res += w
                bank.append(idx)
            if w == 'a' and res == 'cro':
                res += w
                bank.append(idx)
            if w == 'k' and res == 'croa':
                res += w
                bank.append(idx)
        if len(res) == 5:
            for i in res:
                word.remove(i)
                t = True
        else:
            t = False
    print(word)
    if count_A and not word:
        ans = count_A
    else:
        ans = -1

    print(ans)







