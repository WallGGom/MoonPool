KNM = [3, 10, 5]
Stop = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
flag = 0
count = 0

for step in range(3):
    for b2 in range(3, 0, -1):
        if Stop[flag + b2] == 1:
            flag += b2
            count += 1
            Stop[flag + b2] -= 1
            break
        elif Stop[10] == (-1):
            print(count)
        else:
            continue

while Stop[10] == (-1):
    for b2 in range(KNM[2]):
        if Stop[flag + (KNM[2]-b2)] == 1:
            flag += b2
            count += 1
            Stop[flag + b2] -= 1
            break
        elif flag + (KNM[2]-b2) == KNM[1]:
            print(count)


