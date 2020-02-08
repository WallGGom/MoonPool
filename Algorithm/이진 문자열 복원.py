import sys
sys.stdin = open('이진 문자열 복원.txt','r')

T = int(input())

for tc in range(T):
    A, B, C, D = map(int, input().split())
    a = '00'
    b = '01'
    c = '10'
    d = '11'
    res = ''

    if A != 0 and res == '':
        res += '00'
        A -= 1
    elif B != 0 and res == '':
        res += '01'
        B -= 1
    elif C != 0 and res == '':
        res += '10'
        C -= 1
    elif D != 0 and res == '':
        res += '11'
        D -= 1

    t = True
    while t:
        fail = 0
        if res[-1] == '0' and A > 0:
            res += '0'
            A -= 1
        elif res[-1] == '0' and B > 0:
            res += '1'
            B -= 1  
        else:
            fail += 1
        if res[0] == '0' and A > 0:
            res_rev = res[::-1]
            res_rev += '0'
            res = res_rev[::-1]
            A -= 1
        elif res[0] == '0' and C > 0:
            res_rev = res[::-1]
            res_rev += '1'
            res = res_rev[::-1]
            C -= 1 
        else:
            fail += 1
        if res[-1] == '1' and D > 0:
            res += '1'
            D -= 1
        elif res[-1] == '1' and C > 0:
            res += '0'
            C -= 1
        else:
            fail += 1
        if res[0] == '1' and D > 0:
            res_rev = res[::-1]
            res_rev += '1'
            res = res_rev[::-1]
            D -= 1
        elif res[0] == '1' and B > 0:
            res_rev = res[::-1]
            res_rev += '0'
            res = res_rev[::-1]
            B -= 1
        else:
            fail += 1
        if A == 0 and B == 0 and C == 0 and D == 0:
            t = False
        elif fail == 4:
            t = False
            res = 'impossible'
    print('#{} {}'.format(tc+1, res))





    

     