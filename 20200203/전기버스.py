import sys
sys.stdin = open('1일차 - 전기버스.txt', 'r')

T = int(input())


for tc in range(T):
    K, N, M = map(int, input().split()) # K : 스탭, N : 버스 정류장 개수, M : 충전소 좌표
    datalist = list(map(int, input().split())) #공백으로 구분해서 int로 받아서 list를 만든다.

    #1)
    # last, cnt_fill, rest = 0, 0, 0
    # STOPS_Charge = [False]*(N+1)
    # for n in datalist:  STOPS_Charge[n] = True
    # STOPS_Charge[N] = True
    # for stop in range(1, N+1):



    #2)
    # datalist.sort()
    last, cnt_fill, rest = 0, 0, 0
    M = len(datalist)
    for i in range(M):
        if datalist[i] > last + K: rest = -1; break
        if i == (M - 1) and N > last + K or i != (M - 1) and datalist[i+1]> last + K:
            last = datalist[i]
            cnt_fill += 1

    print('#%d %d' % (tc+1,0 if rest < 0 else cnt_fill))



