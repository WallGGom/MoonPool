import sys
sys.stdin = open('세가지 합 구하기.txt', 'r')

T = int(input())
S1 = []
S2 = []
S3 = []
for tc in range(T):
    N = int(input())
    if N % 2 == 0:
        S1.append((1+N)*(N//2))
        S2.append((N*2)*(N//2))
        S3.append(((N+1)*2)*(N//2))
    else:
        S1.append((1+N)*(N//2)+((1+N)//2))
        S2.append((N * 2) * (N // 2)+N)
        S3.append(((N+1)*2)*(N//2)+(N+1))
# print(S1, S2, S3)
for i in range(T):
    print('#{} {} {} {}'.format(i+1, S1[i], S2[i], S3[i]))