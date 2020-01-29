import sys
sys.stdin = open('1일차 - 단순 2진 암호코드.txt', 'r')

def divide_list(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

T = int(input())

for tc in range(T):
    NM = list(map(int, input().split()))
    data = list(input()) #공백으로 구분해서 int로 받아서 list를 만든다.
    a = divide_list(data, 7)
    print(a)


