import sys
sys.stdin = open('파도반 수열.txt','r')

bank = [1, 1, 1]
for n in range(3, 101):
    bank.append(bank[n - 2] + bank[n - 3])

T = int(input())
for t in range(T):
    N = int(input())
    print('#{} {}'.format(t+1, bank[N - 1]))