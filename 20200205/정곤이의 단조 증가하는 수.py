import sys
sys.stdin = open('정곤이의 단조 증가하는 수.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    num = list(map(int, input().split()))
    res = -1
    for i in range(len(num) - 1):
        for j in range(i + 1, len(num)):
            multi = num[i] * num[j]
            # print(multi)
            dan = multi
            while multi >= 10:
                nam1 = multi % 10
                multi //= 10
                nam2 = multi % 10
                if nam1 < nam2:
                    dan = -1
                    break
            if dan > res:
                res = dan

    print('#{} {}'.format(tc+1,res))

    # lst = []
    # for i in range(1, 1 << N):
    #     sub_lst = []
    #     for j in range(N):
    #         if i & (1 << j):
    #             sub_lst.append(num[j])
    #     if len(sub_lst) == 2:
    #         lst.append(sub_lst)
    # # print(lst)
    #
    # result = []
    # for k in range(len(lst) - 1):
    #     if lst[k][0] <= lst[k + 1][0] and lst[k][1] <= lst[k + 1][1]:
    #         result.append(lst[k + 1][0] * lst[k + 1][1])
    #     else:
    #         break
    #
    # if result:
    #     res = result[-1]
    # else:
    #     res = -1
    # print('#{} {}'.format(tc + 1, res))


    # multi = []
    # for i in range(len(num)-1):
    #     num[i], num[0] = num[0], num[i]
    #     for j in range(1, len(num)):
    #         multi.append(num[0]*num[j])
    # print(multi)

    # count = 0
    # for i in range(len(multi)-1):
    #     if multi[i] <= multi[i+1]:
    #         count += 1
    #     elif multi[i] > multi[i+1]:
    #         break
    #
    # if count == 0:
    #     result = -1
    # else:
    #     result = multi[count]
    #
    # print('#{} {}'.format(tc+1, result))

    # count = 0
    # for pic in range(len(lst)):
    #     if lst[pic][0]*lst[pic][1] <= lst[pic+1][0]*lst[pic+1][1]:
    #         count += 1
    #     elif lst[pic][0]*lst[pic][1] > lst[pic+1][0]*lst[pic+1][1]:
    #         break
    #
    #
    # if count == 0:
    #     result = -1
    # else:
    #     result = lst[count][0]*lst[count][1]
    #
    # print('#{} {}'.format(tc+1, res))