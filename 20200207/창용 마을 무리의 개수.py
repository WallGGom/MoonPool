import sys
sys.stdin = open('창용 마을 무리의 개수.txt', 'r')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    bill = []
    for i in range(M):
         bill.append(list(map(int, input().split())))
    print(bill)


    check1 = bill.copy()
    check2 = bill.copy()
    # print(check)

    # bank = []
    # t = True
    # count = 0
    # while t:
    #     for h in check1:
    #         cnt = 0
    #         for know in check2:
    #             if h[1+count] == know[0]:
    #                 h.append(know[1])
    #                 bank.append(h)
    #             else:
    #                 cnt += 1
    #         if len(check2) == cnt:
    #             t = False
    #         print(bank)
    #     count += 1
    # print(bank)


    for h in check1:
        for know in check2:
            if h[-1] == know[0]:
                temp = h + know
                check2.remove(know)
                check2.append(temp)
    print(check2)