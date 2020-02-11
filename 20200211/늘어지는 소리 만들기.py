import sys
sys.stdin = open('늘어지는 소리 만들기.txt','r')

T = int(input())

for tc in range(T):
    word = ['']
    for i in str(input()):
        word.append(i)
    # print(word)

    H = int(input())
    location = list(map(int, input().split()))
    for _ in location:
        word[_] += '-'
    # print(word)

    res = ''
    for pick in word:
        res += pick
    print('#{} {}'.format(tc+1,res))

