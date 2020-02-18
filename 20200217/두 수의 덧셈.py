T = int(input())
bank = []
for tc in range(T):
    A, B = map(int, input().split())
    ans = A + B
    bank.append(ans)

for i in range(T):
    print('#{} {}'.format(i+1, bank[i]))