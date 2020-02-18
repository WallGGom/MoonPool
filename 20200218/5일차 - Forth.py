import sys
sys.stdin = open('5일차 - Forth.txt', 'r')

yun = ['+','*','/','-']


T = int(input())
for tc in range(T):
    res = list(map(str, input().split()))

    hap = 0
    t = True
    count = 0
    ans = ''
    while t:
        for idn, val in enumerate(res[:-1]):
            if val in yun:
                if val == '+':
                    if res[idn - 2].isdigit() and res[idn - 1].isdigit():
                        hap = int(res[idn - 2]) + int(res[idn - 1])
                        res[idn-2] = str(hap)
                        res.pop(idn)
                        res.pop(idn-1)
                        break
                    else:
                        ans = 'error'
                        t = False
                        break
                elif val == '-':
                    if res[idn - 2].isdigit() and res[idn - 1].isdigit():
                        hap = int(res[idn - 2]) - int(res[idn - 1])
                        res[idn-2] = str(hap)
                        res.pop(idn)
                        res.pop(idn-1)
                        break
                    else:
                        ans = 'error'
                        t = False
                        break
                elif val == '*':
                    if res[idn - 2].isdigit() and res[idn - 1].isdigit():
                        hap = int(res[idn - 2]) * int(res[idn - 1])
                        res[idn-2] = str(hap)
                        res.pop(idn)
                        res.pop(idn-1)
                        break
                    else:
                        ans = 'error'
                        t = False
                        break
                elif val == '/':
                    if res[idn - 2].isdigit() and res[idn - 1].isdigit():
                        hap = int(res[idn - 2]) // int(res[idn - 1])
                        res[idn-2] = str(hap)
                        res.pop(idn)
                        res.pop(idn-1)
                        break
                    else:
                        ans = 'error'
                        t = False
                        break
            elif val == '.':
                if len(res) > 2:
                    ans = 'error'
                    t = False
                    break
                else:
                    t = False
                    break

        for i in res:
            if i in yun:
                count += 1
                break
        if count == 0:
            if len(res) > 2:
                ans = 'error'
                t = False
            else:
                t = False
        count = 0

    if ans == '':
        print('#{} {}'.format(tc+1, res[0]))
    else:
        print('#{} {}'.format(tc + 1, ans))