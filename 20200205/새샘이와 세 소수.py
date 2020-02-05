import sys
sys.stdin = open('새샘이와 세 소수.txt', 'r')


T = int(input())

def prime(n): # 소수
    if n < 2:
        return False
    for i in range(2, n):
        if n % i is 0:
            return False
    return True



for tc in range(T):
    N = int(input())
    sosu = []
    for num in range(2, N-3):
        if prime(num):
            sosu.append(num)
    print(sosu)

    combi = []
    for i in sosu:
        for j in sosu:
            for k in sosu:
                sub_combi = []
                sub_combi.append(i)
                sub_combi.append(j)
                sub_combi.append(k)
                combi.append(sub_combi)
    print(combi)





