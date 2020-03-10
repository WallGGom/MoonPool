import sys
sys.stdin = open('원재의 메모리 복구하기.txt','r')

T = int(input())
for tc in range(T):
    bit = input()
    flag = True
    cnt = 0
    for i in bit:
        if i == '0' and flag == True:
            continue
        elif i == '1' and flag == True:
            cnt += 1
            flag = False
        elif i == '0' and flag == False:
            cnt += 1
            flag = True
        elif i == '1' and flag == False:
            continue
    print(f'#{tc+1} {cnt}')