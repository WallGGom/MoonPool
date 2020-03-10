import sys
sys.stdin = open('햄버거 다이어트2.txt','r')

T = int(input())
for tc in range(T):
    N, L = map(int,input().split())
    T_li = list()
    K_li = list()
    for n in range(N):
        T, K = map(int,input().split())
        T_li.append(T)
        K_li.append(K)
    max = 0
    for i in range(1 << N):
        empty = list()
        for j in range(N):
            if i & (1 << j):
                empty.append(K_li[j])
            else:
                empty.append(0)
        print(empty)
        if sum(empty) <= L:
            total = 0
            for idx, r in enumerate(empty):
                if r:
                    total += T_li[idx]
            if total > max:
                max = total
    print('#{} {}'.format(tc+1,max))