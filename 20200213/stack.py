def CRTESTACK() :  return([])
def PUSH(stack,item) :  stack.append(item)
def ISEMPTY(stack) :    return len(stack)==0
def POP(stack) :        return stack.pop(-1) if len(stack) else None
def PEEK(stack) :       return stack[-1] if len(stack) else None

def chk_bracket(lst):
    stack = CRTESTACK()
    bracket = ['(', '{', '[', ')', '}', ']']
    for char in lst:
        if char in bracket[:3]:
            PUSH(stack, char)
        if char in bracket[3:]:
            POP(stack)

    return 'ERROR' if len(stack) else 'GOOD!'

import sys
sys.stdin = open('괄호검사.txt')

T = int(input())

for tc in range(T):
    lst = input()
    print('{}의 괄호 짝은 {}'.format(lst, chk_bracket(lst)))


'''입력예시
2
()()((()))
((()((((()()((()())((())))))))))

출력예시
()()((()))의 괄호 짝은 GOOD!
((()((((()()((()())((())))))))))의 괄호 짝은 GOOD!
'''