import sys
sys.stdin = open('문자열 교집합.txt', 'r')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    temp1 = list(map(str, input().split()))
    temp2 = list(map(str, input().split()))
    temp1.sort()
    temp2.sort()
    # print(temp1)
    # print(temp2)

    cnt = 0
    t = True
    while t:
        if len(temp1) == 0 and len(temp2) == 0:
            t = False
            break
        if temp1[-1] == temp2[-1]:
            cnt += 1
            temp1.pop()
            temp2.pop()
        elif temp1[-1] > temp2[-1]:
            temp1.pop()
        elif temp1[-1] < temp2[-1]:
            temp2.pop()
    
    print(f'#{tc+1} {cnt}')


    
