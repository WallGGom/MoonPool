import sys
sys.stdin = open('현주의 상자 바꾸기.txt', 'r')

T = int(input())

for tc in range(T):
    N, Q = map(int, input().split())
    box = [0]*N
    i = 1
    for _ in range(Q):
        L, R = map(int, input().split())
        for fill in range(L-1,R):
            box[fill] = i
        i += 1
    res = ''
    for j in range(len(box)):
        res += str(box[j]) + ' '

    print('#{} {}'.format(tc+1, res))