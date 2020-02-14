import sys
sys.stdin = open('Digit sum.txt', 'r')

def d_s(n):
    global temp
    for i in n:
        temp += int(i)
    if temp > 9:
        a = temp
        temp = 0
        d_s(str(a))
    return temp

T = int(input())

for tc in range(T):
    n = input()
    temp = 0
    print('#{} {}'.format(tc+1, d_s(n)))