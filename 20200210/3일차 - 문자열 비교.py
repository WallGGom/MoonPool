import sys
sys.stdin = open('3일차 - 문자열 비교.txt', 'r')

T = int(input())

for tc in range(T):
    str1 = str(input())
    str2 = str(input())

    L1 = len(str1)
    L2 = len(str2)

    count = 0
    for i in range(L2-L1+1):
        if str2[i:i+L1] == str1:
            count += 1

    if count >= 1:
        res = 1
    else:
        res = 0
    print('#{} {}'.format(tc+1, res))
