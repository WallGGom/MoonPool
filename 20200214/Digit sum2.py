import sys
sys.stdin = open('Digit sum.txt', 'r')

T = int(input())
bank = []

for tc in range(T):
    n = input()
    temp = 0
    t = True
    while t:
        for i in n:
            temp += int(i)
        if temp <= 9:
            ans = temp
            t = False
        else:
            n = str(temp)
            temp = 0

    bank.append(ans)

for t in range(T):
    print('#{} {}'.format(t+1, bank[t]))