import sys
sys.stdin = open('보물상자 비밀번호.txt', 'r')

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    mulsoe = list(input())
    # print(mulsoe)
    bank = []
    for i in range(N//4):
        mulsoe.append(mulsoe.pop(0))
        for j in range(0,N,N//4):
            bimil = ''.join(mulsoe[j:j+N//4])
            if bimil not in bank:
                # bank.append(int(bimil, 16))
                bank.append(bimil)
    bank.sort()
    # print(bank)
    print(f'#{tc+1} {int(bank[len(bank)-K],16)}')