import sys
sys.stdin = open('5일차 - Forth.txt', 'r')

yun = ['+','-','*','-']
T = int(input())
for tc in range(T):
    data = list(map(str, input().split()))
    data = data[:-1]
    # print(data)
    flag = 0
    bank = []

    for val in data:
        if val.isdigit():
            bank.append(val)

        else:
            try:
                n2, n1 = int(bank.pop()), int(bank.pop())

                if val == '+':
                    top = n1 + n2
                elif val == '-':
                    top = n1 - n2
                elif val == '/':
                    top = n1 // n2
                elif val == '*':
                    top = n1 * n2

                bank.append(top)
            except:
                flag = 1

    if flag == 0 and len(bank) == 1:
        print('#{} {}'.format(tc+1, bank[0]))
    elif flag == 1 or len(bank) > 1:
        print('#{} error'.format(tc+1))
