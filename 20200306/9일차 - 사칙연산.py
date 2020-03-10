import sys
sys.stdin = open('9일차 - 사칙연산.txt', 'r')

def sachick(n):
    if len(Tree[n]) == 2:
        return int(Tree[n][1])
    else:
        n1 = sachick(int(Tree[n][2])-1)
        n2 = sachick(int(Tree[n][3])-1)
        if Tree[n][1] == '+':
            return n1 + n2
        elif Tree[n][1] == '-':
            return n1 - n2
        elif Tree[n][1] == '*':
            return n1 * n2
        elif Tree[n][1] == '/':
            return n1 / n2

T = 10
for tc in range(T):
    N = int(input())
    Tree = []
    for _ in range(N):
        Tree.append(input().split())
    # print(Tree)
    print(f'#{tc+1} {int(sachick(0))}')