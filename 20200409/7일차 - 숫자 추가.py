import sys, copy
sys.stdin = open('7일차 - 숫자 추가.txt', 'r')

T = int(input())

for tc in range(T):
    N, M, L = map(int, input().split())
    suyeol = list(map(int, input().split()))
    for i in range(M):
        cord, num = map(int, input().split())
        suyeol.insert(cord, num)
    print(f'#{tc+1} {suyeol[L]}')
