import sys
sys.stdin = open('햄버거 다이어트.txt','r')

def jaksimsamil(n,s,m):
    global score

    if s > L:
        return

    if m >= score:
        score = m
    
    if n == N:
        return
    else:
        jaksimsamil(n+1,s+Kcal[n][1],m+Kcal[n][0])
        jaksimsamil(n+1,s,m)

T = int(input())
for tc in range(T):
    N, L = map(int, input().split())
    Kcal = []
    for i in range(N):
        Kcal.append(list(map(int, input().split())))
    # print(Kcal)
    score = 0
    sal = 0
    mat = 0
    jaksimsamil(0,sal,mat)
    print(f'#{tc+1} {score}')

