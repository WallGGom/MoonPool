import sys
sys.stdin = open('의석이의 세로로 말해요.txt', 'r')


T = int(input())

for tc in range(T):
    N = 5
    garo = []
    lng = 0
    for _ in range(N):
        word = str(input())
        if len(word) > lng:
            lng = len(word)
        garo.append(word)
    # print(garo)
    # print(lng)
    for i in range(5):
        while len(garo[i]) < lng:
            temp = garo[i]
            temp += '.'
            garo[i] = temp
    # print(garo)

    sero = ['']*lng
    for j in range(5):
        for k in range(lng):
            if not garo[j][k] == '.':
                sero[k] += str(garo[j][k])
    ans = ''.join(sero)

    print('#{} {}'.format(tc+1, ans))






