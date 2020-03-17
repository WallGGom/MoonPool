import sys
sys.stdin = open('정식이의 은행업무.txt','r')

T = int(input())
for tc in range(T):
    A_2 = input()
    A = int(A_2, 2)
    B_3 = input()
    B = int(B_3, 3)
    # print(A_2, A)
    # print(B_3, B)

    res_2 = []
    res_3 = []

    for i in range(1,len(A_2)):
        if A_2[i] == '1':
            res_2.append(A - 2**(len(A_2)-i-1))
        elif A_2[i] == '0':
            res_2.append(A + 2**(len(A_2)-i-1))
    # print(res_2)

    for j in range(len(B_3)):
        if B_3[j] == '1':
            res_3.append(B - 3**(len(B_3)-j-1))
            res_3.append(B + 3**(len(B_3)-j-1))
        elif B_3[j] == '2':
            res_3.append(B - 3**(len(B_3)-j-1))
            res_3.append(B - 2*3**(len(B_3)-j-1))
        elif B_3[j] == '0':
            res_3.append(B + 3**(len(B_3)-j-1))
            res_3.append(B + 2*3**(len(B_3)-j-1))
    # print(res_3)

    for k in res_2:
        if k in res_3:
            print(f'#{tc+1} {k}')