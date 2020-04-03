import sys
sys.stdin = open('13458_시험 감독.txt','r')

N = int(input())
A = list(input().split())
B, C = map(int, input().split())

cnt = 0
for i in range(N):
    temp = int(A[i]) - B
    cnt += 1
    if temp > 0:
        cnt += (temp // C)
        if (temp % C):
            cnt += 1
print(cnt)