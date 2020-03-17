import sys
sys.stdin = open('쥬스 나누기.txt','r')

T = int(input())
for tc in range(T):
    N = int(input())
    res = ''
    for i in range(N):
        res += f'1/{N}' + ' '
    print(f'#{tc+1} {res}')