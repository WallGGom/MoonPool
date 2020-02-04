import sys
sys.stdin = open('한빈이와 Spot Mart.txt', 'r')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    snack = list(map(int, input().split()))

    bank = []
    L = len(snack)

    lst = []
    for i in range(1 << L):
        sub_lst = []
        for j in range(L):
            if i & (1 << j):
                sub_lst.append(snack[j])
        lst.append(sub_lst)

    # print(lst)

    correct_lst = []
    for k in lst:
        if len(k) == 2:
            correct_lst.append(k)

    # print(correct_lst)

    candidate_lst = []
    for l in correct_lst:
        if sum(l) <= M:
            candidate_lst.append(sum(l))

    # print(candidate_lst)

    if candidate_lst:
        result = max(candidate_lst)
    else:
        result = -1

    print('#{} {}'.format(tc+1, result))


