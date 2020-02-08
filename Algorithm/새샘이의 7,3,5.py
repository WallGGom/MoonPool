import sys
sys.stdin = open('새샘이의 7,3,5.txt', 'r')


T = int(input())
for tc in range(T):
    numbers = list(map(int, input().split()))
    numbers.sort()
    # print(numbers)

    num = []
    for i in range(0,len(numbers)-2):
        for j in range(i+1,len(numbers)-1):
            for k in range(j+1, len(numbers)):
                temp = numbers[i] + numbers[j] + numbers[k]
                if not temp in num:
                    num.append(temp)
                temp = 0
    num.sort()
    # print(num)
    print('#{} {}'.format(tc+1,num[-5]))