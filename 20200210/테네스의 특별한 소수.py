import sys
sys.stdin = open('테네스의 특별한 소수.txt','r')

# def prime(num):
#     if num < 2:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

def prime_list(s, n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(s, n) if sieve[i] == True]

T = int(input())

for tc in range(T):
    D, A, B = map(int, input().split())
    count = 0
    sosu = prime_list(A, B)
    # print(sosu)

    for pick in sosu:
        if pick % 10 == D:
            count += 1
            continue
        else:
            while pick >= 10:
                pick //= 10
                if pick % 10 == D:
                    count += 1
                    break

    print('#{} {}'.format(tc+1, count))
