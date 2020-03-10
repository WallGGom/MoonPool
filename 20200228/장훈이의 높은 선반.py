import sys
sys.stdin = open('장훈이의 높은 선반.txt','r')

def kicuteumyun(n,k):
    global mn

    if k >= B and mn > k:
        mn = k

    if n == N:
        return
    else:
        kicuteumyun(n+1,k+S[n])
        kicuteumyun(n+1,k)

T = int(input())

for tc in range(T):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))

    mn = 200000
    kicuteumyun(0,0)
    print(f'#{tc+1} {mn-B}')
