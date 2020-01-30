import sys
sys.stdin = open('간단한 369게임.txt', 'r')

N = int(input())
blank = ""
count = 0
for i in range(1, N+1):
    t = i
    for j in range(len(str(i))):
        if (t % 10) == 3 or (t % 10) == 6 or (t % 10) == 9:
            count += 1
            t //= 10
        else:
            t //= 10
    if count == 0:
        e = str(i)
        blank += '{} '.format(e)
    else:
        blank += ('-'*count + ' ') 
        count = 0
               
print(blank)