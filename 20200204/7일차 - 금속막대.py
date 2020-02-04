import sys
sys.stdin = open('7일차 - 금속막대.txt', 'r')

T = int(input())

for tc in range(T):
    n = int(input())

    Array = list(map(int, input().split()))
    print(Array)
    # print(max(Array))

    se = []
    for i in range(max(Array)+1):
        if Array.count(i) == 1:
            se.append(i)

    # print(se)

    if Array.index(se[0]) % 2 and not Array.index(se[1]) % 2:
        end = Array.index(se[0])
        start = Array.index(se[1])
    else:
        start = Array.index(se[0])
        end = Array.index(se[1])

    # print(start)
    # print(end)



    bank = [[0, 0] for _ in range(n)]
    # print(bank)

    for y in range(n):
        for x in range(2):
            bank[y][x] = Array[(2*y) + x]
    print(bank)

    # star = bank[start // 2]
    # en = bank[(end-1) // 2]
    #
    # mid1 = bank[0]
    # mid2 = bank[-1]
    #
    # bank[0] = star
    # bank[-1] = en
    #
    # bank[start // 2] = mid1
    # bank[(end - 1) // 2] = mid2
    if bank[start // 2] == bank[-1] and bank[(end - 1) // 2] == bank[0]:
        bank[start // 2], bank[(end - 1) // 2] = bank[(end - 1) // 2], bank[start // 2]

    elif bank[start // 2]  == bank[0]:
        bank[(end - 1) // 2], bank[-1] = bank[-1], bank[(end - 1) // 2]

    elif bank[(end - 1) // 2] == bank[0]:
        bank[(end - 1) // 2], bank[-1] = bank[-1], bank[(end - 1) // 2]
        bank[start // 2], bank[0] = bank[0], bank[start // 2]


    else:
        bank[start // 2], bank[0] = bank[0], bank[start // 2]
        bank[(end - 1) // 2], bank[-1] = bank[-1], bank[(end - 1) // 2]


    # print(bank)

    for i in range(n-1):
        for j in range(n):
            if bank[i][1] == bank[j][0]:
                bank[i+1], bank[j] = bank[j], bank[i+1]
    print(bank)

    sol = []

    for Y in range(n):
        for X in range(2):
            sol.append(bank[Y][X])

    # print(sol)
    # print('#{} {}'.format(tc+1, ' '.join(map(str, sol))))