import sys
sys.stdin = open('3일차 - 회문1.txt','r')

T = 10
N = 8

def pall(lst):
    lst_rev = lst[::-1]
    if lst == lst_rev:
        return True
    return False

for tc in range(T):
    K = int(input())
    plane = []
    for _ in range(N):
        plane.append(list(input()))
    # print(plane)
    count = 0
    for y in range(N):
        for x in range(N-K+1):
            bank = []
            for i in range(K):
                bank.append(plane[y][x+i])
            # print(bank)
            if pall(bank):
                count += 1
    # print(count)

    for x in range(N):
        for y in range(N-K+1):
            bank = []
            for j in range(K):
                bank.append(plane[y+j][x])
            # print(bank)
            if pall(bank):
                count += 1
    print('#{} {}'.format(tc+1,count))