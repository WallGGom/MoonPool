import sys
sys.stdin = open('N-Queen.txt','r')

def chaja(garo):
    global cnt
    if garo == N:
        cnt += 1
        return

    for i in range(N):
        t = True
        if sero[i] == 0:
            for y, x in Q.items():
                if abs((y - garo) / (x - i)) == 1:
                    t = False
                    break
            if t:
                sero[i] = 1
                Q[garo] = i
                chaja(garo+1)
                sero[i] = 0
                del Q[garo]

T = int(input())
for tc in range(T):
    N = int(input())
    
    sero = [0]*N
    Q = {}
    cnt = 0
    for x in range(N):
        sero[x] = 1
        Q[0] = x
        chaja(1)
        sero[x] = 0
        del Q[0]
    print(f'#{tc+1} {cnt}')