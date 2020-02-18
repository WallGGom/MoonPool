import sys
sys.stdin = open('최장 증가 부분 수열.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    bank = list(map(int, input().split()))
    # print(bank)
    dp = [1]*N

    for i in range(1, N):
        for j in range(i):
            if bank[j] < bank[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    res = max(dp)
    print('#{} {}'.format(tc+1, res))


