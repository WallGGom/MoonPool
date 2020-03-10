import sys
sys.stdin = open('가능한 시험 점수.txt', 'r')

def sihumsirung(n, hap):
    if hap in visit[n]:
        return
    visit[n][hap] = 1

    if n == N:
        bank.add(hap)
        return
    else:
        sihumsirung(n+1, hap + score[n])
        sihumsirung(n+1, hap)

T = int(input())
for tc in range(T):
    N = int(input())
    score = list(map(int, input().split()))
    # print(score)
    visit = [{} for _ in range(N+1)]
    # print(visit)
    bank = set()
    sihumsirung(0,0)
    
    print(f'#{tc+1} {len(bank)}')
