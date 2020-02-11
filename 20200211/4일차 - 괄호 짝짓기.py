import sys
sys.stdin = open('4일차 - 괄호 짝짓기.txt','r')

T = 10

for tc in range(T):
    N = int(input())
    gwal = input()
    # print(gwal)

    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    l6 = []
    l7 = []
    l8 = []
    for i in gwal:
        if i == '(':
            l1.append(i)
        elif i == ')':
            l2.append(i)
        elif i == '[':
            l3.append(i)
        elif i == ']':
            l4.append(i)
        elif i == '{':
            l5.append(i)
        elif i == '}':
            l6.append(i)
        elif i == '<':
            l7.append(i)
        elif i == '>':
            l8.append(i)

    if len(l1) == len(l2) and len(l3) == len(l4) and len(l5) == len(l6) and len(l7) == len(l8):
        ans = 1
    else:
        ans = 0

    print('#{} {}'.format(tc+1, ans))