import sys
sys.stdin = open('최장 공통 부분 수열.txt', 'r')

T = int(input())

for tc in range(T):
    A, B = map(str, input().split())

    lcs = [[0 for i in range(len(A)+1)] for j in range(len(B)+1)]

    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                lcs[i+1][j+1] = lcs[i][j] + 1
            else:
                lcs[i+1][j+1] = max(lcs[i+1][j], lcs[i][j+1])
    # print(lcs)

    print('#{} {}'.format(tc+1, lcs[len(A)][len(B)]))




