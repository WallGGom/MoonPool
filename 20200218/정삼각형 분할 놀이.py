import sys
sys.stdin = open('정삼각형 분할 놀이.txt','r')

T = int(input())
ans = []
for tc in range(T):
    A, B = map(int, input().split())

    ans.append((A//B)*(A//B))

for i in range(T):
    print('#{} {}'.format(i+1, ans[i]))