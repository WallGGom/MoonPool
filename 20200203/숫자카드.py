import sys
sys.stdin = open('1일차 - 숫자 카드.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    datalist = [int(x) for x in input()]
    Cards = [0]*10
    for n in datalist:
        Cards[n] += 1
    print(Cards)
    max_cnt = 0
    maxi = 0
    for i in range(10):
        if max_cnt < Cards[i]:
            max_cnt = Cards[i]
            maxi = i

    print('#%d %d %d' % (tc+1, i, max_cnt))
