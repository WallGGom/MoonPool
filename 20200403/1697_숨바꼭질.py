import sys
sys.stdin = open('1697_숨바꼭질.txt','r')
     
X, K = map(int, input().split())

visited = [0]*100001
Q = [(X,0)]
visited[X] = 1
ans = 0
if X == K:
    print(ans)
else:
    while Q:
        temp = Q.pop(0)
        t = [temp[0]+1,temp[0]-1,temp[0]*2]
        if K in t:
            ans = temp[1]+1
            break
        for i in t:
            if 0 <= i <= 100000 and visited[i] == 0:
                visited[i] = 1
                Q.append((i,temp[1]+1))
    print(ans)

