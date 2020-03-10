import sys
sys.stdin = open('수영장.txt','r')

def haeum(n, hap):
    global mn
    if hap > mn:
        return

    if n > 11:
        if hap < mn:
            mn = hap
        return


    if jaksimsamil[n]:
        haeum(n+1, hap + jaksimsamil[n]*cost[0])
        haeum(n+1, hap + cost[1])
        haeum(n+3, hap + cost[2])
        haeum(n+12, hap + cost[3])
    else:
        haeum(n+1, hap)

T = int(input())
for tc in range(T):
    cost = list(map(int, input().split()))
    jaksimsamil = list(map(int, input().split()))
    # print(jaksimsamil)
    mn = 1080000
    haeum(0, 0)
    print(f'#{tc+1} {mn}')