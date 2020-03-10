import sys
sys.stdin = open("나는 개구리로소이다.txt")

T = int(input())
for tc in range(T):
    temp = [0] * 5
    gegul = list(input())
    
    n = 1
    t = True
    for ind, txt in enumerate(gegul):
        if not temp[0] >= temp[1] >= temp[2] >= temp[3] >= temp[4]:
            ans = -1
            t = False
            break
        else:
            if txt == 'c':
                temp[0] += 1
                if temp[0] > n:
                    n += 1
            elif txt == 'r':
                temp[1] += 1                
            elif txt == 'o':
                temp[2] += 1
            elif txt == 'a':
                temp[3] += 1
            elif txt == 'k':
                temp[4] += 1
                for j in range(5):
                    temp[j] -= 1
    if t:
        if temp != [0]*5:
            ans = -1
        else:
            ans = n
    print(f'#{tc+1} {ans}')
        