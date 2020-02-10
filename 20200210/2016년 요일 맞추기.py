import sys
sys.stdin = open('2016년 요일 맞추기.txt', 'r')

T = int(input())
cal = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
# print(cal)

for tc in range(T):
    m, d = map(int,input().split())

    days = 0
    for _ in range(1,m):
        days += cal[_]
    # print(days)
    days += d
    # print(days)
    if days % 7 == 0:
        ans = 3
    elif days % 7 == 1:
        ans = 4
    elif days % 7 == 2:
        ans = 5
    elif days % 7 == 3:
        ans = 6
    elif days % 7 == 4:
        ans = 0
    elif days % 7 == 5:
        ans = 1
    elif days % 7 == 6:
        ans = 2
    print('#{} {}'.format(tc+1, ans))