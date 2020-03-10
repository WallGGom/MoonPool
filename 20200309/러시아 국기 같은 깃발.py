import sys
sys.stdin = open('러시아 국기 같은 깃발.txt', 'r')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    flag = []
    color = []
    for _ in range(N):
        temp = input()    
        color.append([temp.count('W'), temp.count('B'), M - (temp.count('W')+temp.count('B'))])
        flag.append(temp)
    # print(flag)
    # print(color)

    for i in range(1,N):
        color[i][0] += color[i - 1][0]
        color[i][1] += color[i - 1][1]
        color[i][2] += color[i - 1][2]
    print(color)

    mn = 50*50
    for w in range(0,N-2):
        for b in range(w+1,N-1):
            n_W = M * (w+1) - color[w][0]
            n_B = M * (b-w) - (color[b][1] - color[w][1])
            n_R = M * ((N-1)-b) - (color[N-1][2] - color[b][2])
            n = n_W + n_B + n_R
            if mn > n:
                mn = n
    print(f'#{tc+1} {mn}')
            
                