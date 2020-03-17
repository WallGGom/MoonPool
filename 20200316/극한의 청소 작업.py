import sys
sys.stdin = open('극한의 청소 작업.txt','r')

sa = [1]
for i in range(1, 12):
    sa.append(10**i + (9 * (sa[i-1])))
# print(sa)

T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    if A < 0 and B > 0:
        t = True
    else:
        t = False
    a = str(abs(A))
    b = str(abs(B))
    temp = [int(a),int(b)]
    for ind, i in enumerate([a,b]):
        for j in range(len(i)):
            if j == 0:
                if int(i[len(i)-j-1]) > 4:
                    temp[ind] -= 1
            else:
                if int(i[len(i)-j-1]) < 4:
                    temp[ind] -= sa[j-1] * int(i[len(i)-j-1])
                else:
                    temp[ind] -= sa[j] - ((10 - int(i[len(i)-j-1]))*sa[j-1])
    if t:
        print(f'#{tc+1} {sum(temp)-1}')
    else:
        print(f'#{tc+1} {abs(temp[1]-temp[0])}')