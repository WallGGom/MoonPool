import sys
sys.stdin = open('4일차 - 종이붙이기.txt', 'r')

def JongE(x):
    if x == N:
        return 1
    if x > N:
        return 0
    return JongE(x + 10) + JongE(x + 20) * 2

T = int(input())
for tc in range(T):
    N = int(input())
    print('#{} {}'.format(tc+1, JongE(0)))