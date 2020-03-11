import sys
sys.stdin = open('늘어지는 소리 만들기.txt', 'r')

T = int(input())
for tc in range(T):
    word = input() + ' '
    L = len(word) - 1
    loc = [0]*(L+1)
    H = int(input())
    temp = list(map(int, input().split()))
    for i in temp:
        loc[i] += 1
    # print(loc)
    
    res = ''
    for ind, w in enumerate(word):
        if loc[ind]:
            res += '-'*loc[ind]
            res += w
        else:
            res += w
    print(f'#{tc+1} {res}')
