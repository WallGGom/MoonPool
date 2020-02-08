T = int(input())

for tc in range(T):
    N = str(input())
    if int(N[-1]) % 2:
        ans = 'Odd'
    else:
        ans = 'Even'

    print('#{} {}'.format(tc+1, ans))