import sys
sys.stdin = open('계산기.txt', 'r')

T = 10
stack = []
yun = ['*', '/', '+', '-']
yun_h = ['*', '/']
yun_l = ['+', '-']
for tc in range(T):
    N = int(input())
    word = input()
    # print(word)
    ans = ''
    for i in word:
        if i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                ans += stack.pop()
            if stack[-1] == '(':
                stack.pop()
        elif not i in yun:
            ans += i
        elif i in yun:
            if i in yun_h and stack[-1] in yun_l:
                stack.append(i)
            elif i in yun_l and stack[-1] in yun_h and stack[0] == '(':
                t = True
                while t:
                    ans += stack.pop()
                    if stack[-1] in '(':
                        t = False
                stack.append(i)
            elif i in yun_h and stack[-1] in yun_h and stack[0] == '(':
                t = True
                while t:
                    ans += stack.pop()
                    if stack[-1] in yun_l or stack[-1] == '(':
                        t = False
                stack.append(i)
            else:
                stack.append(i)

    if len(stack) != 0:
        while len(stack) != 0:
            a = stack.pop()
            if a != '(':
                ans += a
    res = list(ans)
    # print(res)
    hap = 0
    t = True
    count = 0
    while t:
        for idn, val in enumerate(res):
            if val in yun:
                if val == '+':
                    hap = int(res[idn - 2]) + int(res[idn - 1])
                    res[idn-2] = hap
                    res.pop(idn)
                    res.pop(idn-1)
                    break
                elif val == '-':
                    hap = int(res[idn - 2]) - int(res[idn - 1])
                    res[idn - 2] = hap
                    res.pop(idn)
                    res.pop(idn - 1)
                    break
                elif val == '*':
                    hap = int(res[idn - 2]) * int(res[idn - 1])
                    res[idn - 2] = hap
                    res.pop(idn)
                    res.pop(idn - 1)
                    break
                elif val == '/':
                    hap = int(res[idn - 2]) / int(res[idn - 1])
                    res[idn - 2] = hap
                    res.pop(idn)
                    res.pop(idn - 1)
                    break

        for i in res:
            if i in yun:
                count += 1
                break
        if count == 0:
            t = False
        count = 0
    print('#{} {}'.format(tc+1, *res))
