import sys, copy
sys.stdin = open('7일차 - 수열 합치기.txt', 'r')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    total = list(input().split())
    # print(total)
    for _ in range(M-1):
        i = list(input().split())
        for j in total:
            if int(j) > int(i[0]):
                ind = total.index(j)
                total[ind:ind] = i
                break
        else:
            total.extend(" ".join(i).split())
    res = f'#{tc+1} '
    for l in range(10):
        res += total[-1-l] + ' '
    print(res)
