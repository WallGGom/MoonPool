import sys
sys.stdin = open('건초더미.txt','r')

T = int(input())
for tc in range(T):
    N = int(input())
    guncho = []
    res = 0
    for i in range(N):
        temp = int(input())
        guncho.append(temp)
        res += temp
    
    ans = 0
    for j in guncho:
        ans += abs(j - (res // N))
    print(f'#{tc+1} {ans//2}')
