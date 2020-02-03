
# N = int(input())
array = [[3,2,1,2,4,1],[2,1,2,1,2,1],[3,2,3,2,1,4],[2,3,4,3,4,1],[3,4,3,4,3,4],[2,3,4,3,1,4]]
# array = [[0]*6]*6 # 왜이럴까?



for y in range(6):
    for x in range(6):
        if y <= 2 and x <= 2:
            array[y][x] = 2
        elif y <= 2 and x > 2:
            array[y][x] = 1
        elif y > 2 and x <= 2:
            array[y][x] = 3
        elif y > 2 and x > 2:
            array[y][x] = 4


for i in range(6):
    print(' '.join(map(str,array[i])))