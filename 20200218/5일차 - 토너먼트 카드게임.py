import sys
sys.stdin = open('5일차 - 토너먼트 카드게임.txt', 'r')

T = int(input())

def winner(A, B):
    if card[A] == 1:
        if card[B] == 1:
            return A
        elif card[B] == 2:
            return B
        elif card[B] == 3:
            return A
    elif card[A] == 2:
        if card[B] == 2:
            return A
        elif card[B] == 3:
            return B
        elif card[B] == 1:
            return A
    elif card[A] == 3:
        if card[B] == 3:
            return A
        elif card[B] == 1:
            return B
        elif card[B] == 2:
            return A
    else:
        return B


def match(i, j):
    if i == j:
        return i

    l = match(i, (i + j) // 2)
    r = match((i + j) // 2 + 1, j)
    a = winner(l,r)
    return a
    # return stack.append([l,r])

for tc in range(T):
    N = int(input())
    card = list(map(int, input().split()))
    stack = []
    i = 0
    j = N - 1
    # match(i,j)
    # # print(card)
    # # print(stack[:-1])
    print(match(i,j)+1)
    # print(winner(None,None))























