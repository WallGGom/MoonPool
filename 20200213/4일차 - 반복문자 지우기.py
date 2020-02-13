import sys
sys.stdin = open('4일차 - 반복문자 지우기.txt', 'r')

T = int(input())

for tc in range(T):
    word = input()
    stack = []
    for i in word:
        if not stack:
            stack.append(i)
        elif i != stack[-1]:
            stack.append(i)
        elif i == stack[-1]:
            stack.pop()
    print('#{} {}'.format(tc+1,len(stack)))
