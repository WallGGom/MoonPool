import sys
sys.stdin = open('세상의 모든 팰린드롬.txt','r')

T = int(input())

for tc in range(T):
    word = list(input())
    for idx, w in enumerate(word):
        if w == '?':
            word[-idx-1] = '?'

    check = ''.join(word)
    # print(check)
    if check == check[::-1]:
        ans = 'Exist'
    else:
        ans = 'Not exist'

    print('#{} {}'.format(tc+1, ans))
