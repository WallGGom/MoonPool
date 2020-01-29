import sys
sys.stdin = open('달팽이 숫자.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    blank = [0]*(N**2)
    num = [0]*(N**2)

    for step in range(N**2):
        blank[step] = step + 1

    print(blank)

for pick in range(N):
    for i in range(N**2):



    # for i in range(N):

