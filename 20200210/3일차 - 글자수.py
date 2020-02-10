import sys
sys.stdin = open('3일차 - 글자수.txt', 'r')

T = int(input())

for tc in range(T):
    str1 = str(input())
    str2 = str(input())

    lst_count = []
    for y in str1:
        count = 0
        for x in str2:
            if y == x:
                count += 1
        lst_count.append(count)
    # print(lst_count)
    print('#{} {}'.format(tc+1, max(lst_count)))

