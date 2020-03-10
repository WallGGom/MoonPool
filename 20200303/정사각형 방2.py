import sys
sys.stdin = open("정사각형 방.txt")

T = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
 
def f(i,j):
 
    global cnt
    for di in range(4):
        if -1<i+dy[di]<N and -1<j+dx[di]<N:
            if arr[i+dy[di]][j+dx[di]]-arr[i][j] == 1:
                cnt += 1
                f(i+dy[di],j+dx[di])
 
for test in range(1,T+1):
    N = int(input())
    arr = []
    ans = []
    ans1 = []
    for i in range(N):
        arr.append(list(map(int,input().split())))
 
    max = 1
    for i in range(N):
        for j in range(N):
            sta_flag = 1
            for k in range(4):
                if -1 < i + dy[k] < N and -1 < j + dx[k] < N:
                    if arr[i][j]-arr[i+dy[k]][j+dx[k]] == 1:
                        sta_flag = 0
                        break
            if sta_flag == 1:
                cnt = 1
                f(i,j)
                if max < cnt:
                    max = cnt
                    ans.append(cnt)
                    ans1.append(arr[i][j])
                elif max == cnt and ans1:
                    ans.append(cnt)
                    ans1.append(min(ans1[-1],arr[i][j]))
 
 
    # print(ans)
    # print(ans1)
 
    print('#{}'.format(test),ans1[-1],ans[-1])