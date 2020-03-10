import sys
sys.stdin = open('올림픽 종목 투표.txt','r')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # print(A)
    # print(B)
    res = [0]*N
    for b in B:
        for idx, a in enumerate(A):
            if a <= b:
                res[idx] += 1
                break
    print(f'#{tc+1} {res.index(max(res))+1}')