import sys
sys.stdin = open('3일차 - 회문2.txt','r')

T = 10
N = 100


def pall(lst):
    lst_rev = lst[::-1]
    if lst == lst_rev:
        return True
    return False


for tc in range(T):
    TC = int(input())
    plane = []
    for _ in range(N):
        plane.append(list(input()))
    # print(plane)
    count = 0
    ans = []
    t1 = True
    Kx = 99
    while Kx > 0 and t1:
        for y in range(N):
            for x in range(N - Kx + 1):
                bank = []
                for i in range(Kx):
                    bank.append(plane[y][x + i])
                # print(bank)
                if pall(bank):
                    ans.append(len(bank))
                    t1 = False
                    Kx = 0
                    break
        Kx -= 1

    t2 = True
    Ky = 99
    while Ky > 0 and t2:
        for x in range(N):
            for y in range(N - Ky + 1):
                bank = []
                for j in range(Ky):
                    bank.append(plane[y + j][x])
                # print(bank)
                if pall(bank):
                    ans.append(len(bank))
                    t2 = False
                    Ky = 0
                    break
        Ky -= 1

    print('#{} {}'.format(TC, max(ans)))
