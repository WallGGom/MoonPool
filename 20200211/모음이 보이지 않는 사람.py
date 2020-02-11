import sys
sys.stdin = open('모음이 보이지 않는 사람.txt', 'r')

T = int(input())
mo = 'aeiou'

for tc in range(T):
    word = input()
    res = ''
    for p in word:
        if not p in mo:
            res += p
    print('#{} {}'.format(tc+1, res))