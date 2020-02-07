import sys
sys.stdin = open('수의 새로운 연산.txt', 'r')

N = 270
plane = {}
stack = 0
stair = 1
count = 0
for y in range(N):
    step = 2 + count
    for x in range(N):
        if x == 0 and y == 0:
            plane[x+1, y+1] = 1
        elif x == 0 and y > 0:
            plane[x+1, y+1] = plane[x+1, y] + stair
            stair += 1
        else:
            plane[x+1, y+1] = plane[x, y+1] + step
            step += 1
    count += 1
# print(plane)

T = int(input())
for tc in range(T):
    p, q = list(map(int, input().split()))

    for key, val in plane.items():
        if val == p:
            location1 = key
        if val == q:
            location2 = key

    # print(location1)
    # print(location2)

    print('#{} '.format(tc+1), end = '')
    print(plane[location1[0]+location2[0],location1[1]+location2[1]])


