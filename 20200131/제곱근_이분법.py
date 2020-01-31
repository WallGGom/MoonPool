y = float(input())

z = y
x = 1

lis = [x, y, z]

# lis[2] = (lis[2] + lis[0])/2
while (lis[2]**2) > y > (lis[0]**2) and abs(lis[2] - lis[0]) > 0.0001:
    if ((lis[2] + lis[0])/2)**2 <= lis[1]:
        lis[0] = (lis[2] + lis[0])/2
    elif ((lis[2] + lis[0])/2)**2 > lis[1]:
        lis[2] = (lis[2] + lis[0])/2

# print('%0.3f' % lis[0])
print(f'{lis[0]:.4}')