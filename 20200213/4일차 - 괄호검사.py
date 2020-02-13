import sys
sys.stdin = open('4일차 - 괄호검사.txt', 'r')

T = int(input())
for tc in range(T):
    word = input()
    bank = []
    ans = 1
    for i in word:
        if i == '(' or i == '{':
            bank.append(i)
        elif i == ')' or i == '}':
            if len(bank) == 0:
                bank.append(1)
                break
            elif (i == ')' and bank[-1] != '(') or (i == '}' and bank[-1] != '{'):
                ans = 0
                break
            else:
                bank.pop()
    if bank:
        ans = 0
    print('#{} {}'.format(tc+1, ans))