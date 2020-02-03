array = [[9,20,2,18,11],[19,1,25,3,21],[8,24,10,17,7],[15,4,16,5,6],[12,13,22,23,14]]

for y in range(5):
    for x in range(5):
        if y == 0:
            array[y][x] = (x + 1)
        elif x == 4:
            array[y][x] = (y + 5)
        elif y == 4:
            array[y][x] = (13 - x)
        elif x == 0 and 0 < y < 4:
            array[y][x] = (17 - y)
        elif y == 1 and 0 < x < 4:
            array[y][x] = (16 + x)
        elif x == 3 and 1 < y < 4:
            array[y][x] = (18 + y)
        elif y == 3 and 0 < x < 3:
            array[y][x] = (24 - x)
        elif y == 2 and 0 < x < 3:
            array[y][x] = (23 + x)

for i in range(5):
    print(' '.join(map(str,array[i])))