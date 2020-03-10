import sys
sys.stdin = open('적고 지우기.txt','r')

T = int(input())

for tc in range(T):
    bank = []
    for i in input():
        if i not in bank:
            bank.append(i)
        else:
            bank.remove(i)
    print(f'#{tc+1} {len(bank)}')
