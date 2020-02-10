import sys
sys.stdin = open('[Professional] 합.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    num = list(map(int, input().split()))
    # print(num)

    for i in range(N-1):
        if num[i] > 0 and num[i] + num[i+1] > 0:
            num[i+1] += num[i]

    print('#{} {}'.format(tc+1, max(num)))