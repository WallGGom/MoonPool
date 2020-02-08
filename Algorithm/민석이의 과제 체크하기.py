T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    No_HW = list(map(int, input().split()))
    HW = [0]*N
    for num in No_HW:
        HW[num-1] = 1
    res = ''
    for idx, val in enumerate(HW):
        if val == 0:
            res += str(idx+1) + ' '
    print('#{} {}'.format(tc+1, res))