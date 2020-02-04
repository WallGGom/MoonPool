import sys
sys.stdin = open('2일차 - 부분집합의 합.txt', 'r')

T = int(input())
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12]
L = len(num)

lst = []
for i in range(1 << L):
    sub_lst = []
    for j in range(L):
        if i & (1 << j):
            sub_lst.append(num[j])
    lst.append(sub_lst)
# print(lst)

for tc in range(T):
    N, K = map(int, input().split())
    # print(N, K)

    len_lst = []
    for k in lst:
        if len(k) == N:
            len_lst.append(k)

    result = 0
    for l in len_lst:
        if sum(l) == K:
            result += 1

    print('#{} {}'.format(tc+1, result))





