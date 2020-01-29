import sys
sys.stdin = open('1일차 - 숫자 카드.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    card = input()
    num = [0] * 10

    for k in range(N):
        num[int(card[k])] += 1
    print(num)

    MX_index = 0
    MX_num = 0
    for i in range(len(num)-1, -1, -1):
        if num[i] > MX_index:
            MX_index = num[i]
            MX_num = i
    print('#{} {} {}'.format(tc+1, MX_num, MX_index))

