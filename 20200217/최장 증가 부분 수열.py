import sys
sys.stdin = open('최장 증가 부분 수열.txt', 'r')

T = int(input())
temp = []
for tc in range(T):
    N = int(input())
    bank = list(map(int, input().split()))
    temp = []
    m = 0
    for i in bank[:-1]:
        a = i
        shift = 1
        for step in range(len(bank)-1,0,-1):
            count = 0
            for j in bank[shift+bank.index(i):shift+bank.index(i)+step]:
                if i < j:
                    i = j
                    count += 1
            shift += 1
            i = a
            if count > m:
                m = count
    temp.append(m)
for i in temp:
    x = 1
    print('#{} {}'.format(x, i+1))
    x += 1
