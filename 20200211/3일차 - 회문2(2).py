import sys
sys.stdin = open('3일차 - 회문2.txt','r')

def count_p(arr):
    global max_len

    for i in range(L):
        W = arr[i]

        idx = 100
        while idx > 0:
            if idx <= max_len:
                break

            for j in range(L - idx + 1):
                w = W[j:j + idx]
                if w == w[::-1]:
                    if max_len < idx:
                        max_len = idx
            idx -= 1


for _ in range(10):
    case = input()
    max_len = 0

    L = 100
    B = []
    for _ in range(L):
        B.append([x for x in input()])
    V = list(zip(*B))
    count_p(B)
    count_p(V)
    print('#{} {}'.format(case, max_len))