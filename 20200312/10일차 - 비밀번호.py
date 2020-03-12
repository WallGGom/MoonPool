import sys
sys.stdin = open('10일차 - 비밀번호.txt','r')

T = 10
for tc in range(T):
    N, PW = map(str, input().split())
    N = int(N)
    PW = list(PW)
    # print(PW)
    t1 = True
    bank = []
    s = 0
    while t1:
        for i in range(s,len(PW)-1):
            if PW[i] == PW[i+1]:
                s = i-1
                bank.append(i)
                bank.append(i+1)
                break
        else:
            t1 = False
        while bank:
            PW.pop(bank.pop())
    
    print(f'#{tc+1} {"".join(PW)}')