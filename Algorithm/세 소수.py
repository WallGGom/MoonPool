import sys
sys.stdin = open('세 소수.txt', 'r')


T = int(input())

def prime(n): # 소수
    # if n < 2:
    #     return False
    for i in range(2, n):
        if n % i is 0:
            return False
    return True

for tc in range(T):
    N = int(input())
    sosu = [2]
    for num in range(3, N-3, 2):
        if prime(num):
            sosu.append(num)
    # print(sosu)

    count = 0
    for i in sosu:
        for j in sosu[sosu.index(i):]:
            for k in sosu[sosu.index(j):]:
                if N == i+j+k:
                    count += 1
       
    print('#{} {}'.format(tc+1, count))
 



    # combi = []
    # for i in sosu:
    #     for j in sosu:
    #         for k in sosu:
    #             sub_combi = []
    #             sub_combi.append(i)
    #             sub_combi.append(j)
    #             sub_combi.append(k)
    #             sub_combi.sort()
    #             combi.append(sub_combi)
    # print(combi)

    # for i in range(len(combi)):
    #     combi[i].sort()

    # new_com = []
    # for j in range(len(combi)):
    #     if not combi[j] in new_com:
    #         new_com.append(combi[j])
    # # print(new_com)

    # count = 0
    # for k in new_com:
    #     if sum(k) == N:
    #         count += 1
    # # print(count)

    # print('#{} {}'.format(tc+1, count))
