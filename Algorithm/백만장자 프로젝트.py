import sys
sys.stdin = open('백만장자 프로젝트.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    pocket = price[-1]

    black = 0

    for i in range(N-2,-1,-1):
        if pocket > price[i]:
            black += pocket - price[i]

        elif pocket < price[i]:
            pocket = price[i]

    print('#{} {}'.format(tc+1,black))

        

