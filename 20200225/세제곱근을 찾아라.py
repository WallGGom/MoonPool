T = int(input())

for tc in range(T):
    N = int(input())

    for i in range(1,int(N**(1/3)+2)):
        if (N == i**3):
            ans = i
            break
        else:
            ans = -1
    print('#{} {}'.format(tc+1, ans))