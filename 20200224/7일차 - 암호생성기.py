import sys
sys.stdin = open('7일차 - 암호생성기.txt', 'r')

T = 10

for t in range(T):
    tc = int(input())
    password = list(map(int, input().split()))
    # print(password)

    t = True
    while t:
        for i in range(1, 6):
            if password[0] - i <= 0:
                password.pop(0)
                password.append(0)
                t = False
                break
            else:
                password.append(password.pop(0)-i)
    res = ''
    for i in password:
        res += str(i) + ' '
    print(f'#{tc} {res}')