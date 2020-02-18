T = 10
stack = []
yun = ['*', '/', '+', '-']
yun_h = ['*', '/']
yun_l = ['+', '-']
for tc in range(T):
    N = int(input())
    word = input()
    print(word)
    for i in word:
        if i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                print(stack.pop(), end='')
            if stack[-1] == '(':
                stack.pop()
        elif not i in yun:
            print(i, end='')
        elif i in yun:
            if i in yun_h and stack[-1] in yun_l:
                stack.append(i)
            elif i in yun_l:
                stack.append(i)
            elif i in yun_h and stack[-1] in yun_h and stack[0] == '(':
                t = True
                while t:
                    print(stack.pop(), end='')
                    if stack[-1] in yun_l:
                        t = False
                stack.append(i)
            else:
                stack.append(i)

    if len(stack) != 0:
        while len(stack) != 0:
            a = stack.pop()
            if a != '(':
                print(a, end='')
    print()