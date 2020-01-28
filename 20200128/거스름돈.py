a = int(input())
c_500 = 500
c_100 = 100
c_50 = 50
c_10 = 10

for i in range(33):
    if a - (c_500*i) < 0:
        num_500 = i
        break
print('500원 %d개'% (num_500 - 1))

for j in range(33):
    if (a - (c_500*(num_500-1))) - (c_100*j) < 0:
        num_100 = j
        break
print('100원 %d개'% (num_100 - 1))

for k in range(33):
    if ((a - (c_500*(num_500-1))) - (c_100*(num_100 - 1))) - (c_50*k) < 0:
        num_50 = k
        break
print('50원 %d개'% (num_50 - 1))

for l in range(33):
    if (((a - (c_500 * (num_500 - 1))) - (c_100 * (num_100-1))) - (c_50 * (num_50-1))) - (c_10 * l) < 0:
        num_10 = l
        break
print('10원 %d개'% (num_10 - 1))