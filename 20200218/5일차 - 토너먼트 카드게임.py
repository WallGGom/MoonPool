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
    # return winner(first, second)
    return stack.append([l, r])

for tc in range(T):
    N = int(input())
    card = list(map(int, input().split()))
    stack = []
    i = 0
    j = N - 1
    match(i,j)
    print(stack)
    # print(match(i,j))

    # while t:
    #     match(i, j)
    #     # print(stack)
    #     for idx, val in enumerate(stack):
    #         stack[idx] = winner(card[val[0]],card[val[1]])
    #     # print(stack)
    #     if len(stack) == 1:
    #         t = False
    #         break
    #     card = stack
    #     stack = []
    #     i = 0
    #     j = len(card)-1
    # print(stack)





















