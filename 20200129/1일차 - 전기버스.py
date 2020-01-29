import sys
sys.stdin = open('1일차 - 전기버스.txt', 'r')

T = int(input())


for tc in range(T):
    KNM = list(map(int, input().split()))
    Stop = [0] * (KNM[1]+1)
    Bus_stop = list(map(int, input().split())) #공백으로 구분해서 int로 받아서 list를 만든다.
    # print(KNM[2])
    for b1 in range(KNM[2]):
        Stop[Bus_stop[b1]] += 1
    # print(Stop)
    start = 0
    step = KNM[0]
    count = 0
    t = True

    while t:
        fail = 0 # 제일 밑 if 구문이 끝나면 fail을 초기화
        for i in range(start + 1, step + 1):
            if Stop[i] == 1:
                    start = i
            else:
                    fail += 1
        
        # for 구문이 끝나면 start에 i(제일 먼 충전소)가 저장되어 나온다. 
        step = start + KNM[0] # 출발점이 i로 밀린만큼 i 에서 KNM[0]만큼 도착점을 늘려준다.
        count += 1

        if fail == KNM[0]:
            count = 0
            t = False # 반복 off
        if step >= KNM[1]:
            t = False # 반복 off
    print('#{} {}'.format(tc+1, count))







