import sys
sys.stdin = open('3일차 - 회문.txt', 'r')

def pall(word):
    if word == word[::-1]:
        return True

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    res = ''
    lst = []
    for i in range(N):
        W = str(input())
        lst.append(W)

        for step in range(N-M+1):
            word = W[step:M+step]
            if pall(word):
                res += word

    for x in range(N):
        W2 = ''
        for y in range(N):
            W2 += lst[y][x]

        for step in range(N-M+1):
            word = W2[step:M+step]
            if pall(word):
                res += word
    # print(res)
    print('#{} {}'.format(tc+1, res))
