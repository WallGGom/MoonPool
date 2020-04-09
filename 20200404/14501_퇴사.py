import sys
sys.stdin = open('14501_퇴사.txt','r')

def sangdam(day, pay):
    global MX
    if day == N:
        if MX < pay:
            MX = pay
            return
    else:
        if day+T[day] <= N:
            sangdam(day+T[day], pay+P[day])
        if day+1 <= N:
            sangdam(day+1,pay)


N = int(input())
T = []
P = []
for i in range(N):
    t , p = map(int, input().split())
    T.append(t)
    P.append(p)
# print(T)
# print(P)
MX = 0
sangdam(0,0)
print(MX)
