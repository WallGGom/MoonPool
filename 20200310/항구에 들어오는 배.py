import sys
sys.stdin = open('항구에 들어오는 배.txt','r')

T = int(input())
for tc in range(T):
    N = int(input())
    hanggu = []
    for _ in range(N):
        hanggu.append(int(input()))
    # print(hanggu)

    jugi = []
    for i in range(1,N):
        jugi.append(hanggu[i]-hanggu[0])
    # print(jugi)

    for j in jugi:
        for k in jugi[jugi.index(j)+1:]:
            if k % j == 0:
                jugi.remove(k)
    print(f'#{tc+1} {len(jugi)}')