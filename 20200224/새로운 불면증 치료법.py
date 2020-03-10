import sys
sys.stdin = open('새로운 불면증 치료법.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    t = True
    bank = [0]*10
    cnt = 0
    while t:
        cnt += 1
        temp = N * (cnt)
        for i in str(temp):
            if bank[int(i)] == 0:
                bank[int(i)] = 1
                if bank == [1]*10:
                    t = False
                    break
    print(f'#{tc+1} {temp}')
                    