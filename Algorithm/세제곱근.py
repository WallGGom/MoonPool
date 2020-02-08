import sys
sys.stdin = open('세제곱근.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())

    for i in range(1,int(N**(1/3))+1):
        if (N == i**3):
            ans = i
        else:
            ans = -1
    print('#{} {}'.format(tc+1, ans))
