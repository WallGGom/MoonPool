import sys
sys.stdin = open('자기 방으로 돌아가기.txt','r')

T = int(input())

for tc in range(T):
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(list(map(int, input().split())))
    # print(lst)
    aisle = [0]*201
    for i in lst:
        if i[0] > i[1]:
            i[0], i[1] = i[1], i[0]
        if i[0] % 2 == 0:
            if i[1] % 2 == 0:
                for step in range((i[0])//2,(i[1]//2)+1):
                    aisle[step] += 1
            else:
                for step in range((i[0])//2,((i[1])//2+1)+1):
                    aisle[step] += 1
        else:
            if i[1] % 2 == 0:
                for step in range((i[0])//2+1,(i[1]//2)+1):
                    aisle[step] += 1
            else:
                for step in range((i[0])//2+1,((i[1])//2+1)+1):
                    aisle[step] += 1

    print(f'#{tc+1} {max(aisle)}')

