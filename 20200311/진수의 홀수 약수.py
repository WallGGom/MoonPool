import sys
sys.stdin = open('진수의 홀수 약수.txt', 'r')

T = int(input())

bank = [0]*1000001
for i in range(1,1000000,2):
    for j in range(1,(1000000//i)+1):
        bank[(i*j)] += i
for k in range(1,1000001):
    bank[k] += bank[k-1]

res = []
for tc in range(T):
    L, R = map(int, input().split())
    res.append(f'#{tc+1} {bank[R]-bank[L-1]}')

print('\n'.join(res))
    

