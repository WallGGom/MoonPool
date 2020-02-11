import sys
sys.stdin = open('세상의 모든 팰린드롬 2.txt','r')

T = int(input())

for tc in range(T):
    word = input()
    ans = 'Exist'
    for i in range(len(word)//2):
        if word[i] == '*' or word[(len(word)-1) - i] == '*':
            break
        if word[i] != word[(len(word) - 1) - i] and word[i] != '*' and word[(len(word) - 1) - i] != '*':
            ans = 'Not exist'

    print('#{} {}'.format(tc+1, ans))















# def ispalin(word):
#     ans = 'Exist'
#     for i in range(len(word) // 2):
#         if word[i] == '*' or word[len(word) - 1 - i] == '*':
#             break
#         if word[i] != word[len(word) - 1 - i] and word[i] != '*' and word[len(word) - 1 - i] != '*':
#             ans = 'Not exist'
#             return ans
#     return ans
#
#
# T = int(1)
# for TC in range(T):
#     target = 'abc*asdaasdcb'
#     print("#{} {}".format(TC + 1, ispalin(target)))