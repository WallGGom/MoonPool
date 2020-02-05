import sys
sys.stdin = open('다솔이의 월급 상자.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    wallgeup = []
    for case in range(N):
        money = list(map(float, input().split()))
        wallgeup.append(money[0]*money[1])

    # print(wallgeup)
    final = sum(wallgeup)
    print('#{} {:.6f}'.format(tc+1, final))
