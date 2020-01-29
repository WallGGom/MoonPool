import sys
sys.stdin = open('1일차 - 구간합.txt', 'r')

T = int(input())

for tc in range(T):
    NM = list(map(int, input().split()))
    data = list(map(int, input().split())) #공백으로 구분해서 int로 받아서 list를 만든다.
    Sm_list = [0]*(NM[0]-NM[1]+1)

    for k in range(NM[0]-NM[1]+1):
        Sm_list[k] = sum(data[k:k+NM[1]]) # 구간합을 리스트에 저장
    # print(Sm_list)

    for i in range(len(Sm_list)):
        for j in range(i + 1, len(Sm_list)):
            if Sm_list[i] > Sm_list[j]:
                Sm_list[i], Sm_list[j] = Sm_list[j], Sm_list[i] # 리스트를 정렬
    # print(Sm_list)

    MX = Sm_list[len(Sm_list)-1]
    # print(MX)
    mn = Sm_list[0]
    # print(mn)

    print('#{} {}'.format(tc+1, MX - mn))