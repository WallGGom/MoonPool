# import random
#
# array = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
# test = array
# # bank = [0]*25
# # for i in range(25):
# #     j = random.choice(range(1, 50))
# #     bank[i] = j
# # random.shuffle(bank)
#
# for y in range(5):
#     for x in range(5):
#         test[y][x] = random.choice(range(1, 50))

test = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
total = 0

for y in range(5):
    for x in range(5):
        if (x == 0) and (y == 0):
            total += abs(test[y][x] - test[y+1][x]) + abs(test[y][x]-test[y][x+1])
        elif (x == 0) and (y == 4):
            total += abs(test[y][x] - test[y - 1][x]) + abs(test[y][x] - test[y][x + 1])
        elif (x == 4) and (y == 0):
            total += abs(test[y][x] - test[y + 1][x]) + abs(test[y][x] - test[y][x - 1])
        elif (x == 4) and (y == 4):
            total += abs(test[y][x] - test[y - 1][x]) + abs(test[y][x] - test[y][x - 1])
        elif (x == 0) and (0 < y < 4):
            total += abs(test[y][x]-test[y+1][x]) + abs(test[y][x]-test[y-1][x]) + abs(test[y][x]-test[y][x+1])
        elif (x == 4) and (0 < y < 4):
            total += abs(test[y][x]-test[y+1][x]) + abs(test[y][x]-test[y-1][x]) + abs(test[y][x]-test[y][x-1])
        elif (y == 0) and (0 < x < 4):
            total += abs(test[y][x]-test[y][x+1]) + abs(test[y][x]-test[y][x-1]) + abs(test[y][x]-test[y+1][x])
        elif (y == 4) and (0 < x < 4):
            total += abs(test[y][x]-test[y][x+1]) + abs(test[y][x]-test[y][x-1]) + abs(test[y][x]-test[y-1][x])
        else:
            total += abs(test[y][x] - test[y + 1][x]) + abs(test[y][x] - test[y - 1][x]) + abs(test[y][x] - test[y][x + 1]) + abs(test[y][x] - test[y][x - 1])

# if (x = 0 or x = 5) and (y = 0 or y = 5):

print(total)


