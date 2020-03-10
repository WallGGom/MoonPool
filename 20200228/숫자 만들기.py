import sys
sys.stdin = open('숫자 만들기.txt','r')

def sachick(n,ans):
    if ysj == [0]*4:
        res.append(ans)
        return
    
    if ysj[0] > 0:
        ysj[0] -= 1
        sachick(n+1,int(ans+num[n+1]))
        ysj[0] += 1
    if ysj[1] > 0:
        ysj[1] -= 1
        sachick(n+1,int(ans-num[n+1]))
        ysj[1] += 1
    if ysj[2] > 0:
        ysj[2] -= 1
        sachick(n+1,int(ans*num[n+1]))
        ysj[2] += 1
    if ysj[3] > 0:
        ysj[3] -= 1
        sachick(n+1,int(ans/num[n+1]))
        ysj[3] += 1

T = int(input())

for tc in range(T):
    N = int(input())
    ysj = list(map(int, input().split()))
    num = list(map(int, input().split()))
    res = []
    # print(ysj)
    # print(num)
    sachick(0,num[0])
    # print(res)
    print(f'#{tc+1} {max(res)-min(res)}')