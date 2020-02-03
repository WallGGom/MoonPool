import random

N = int(input())

array = [0]*N

for i in range(N):
    array[i] = random.choice(range(-(2*N),(2*N)+1))

print(array)

storage = array
a = []
bank = []

count = 0

# t = True
# while t:
#     for num in range(1, N+1):
#         storage = array
#         for j in range(N - num + 1):
#             a = random.sample(storage, num)
#             storage.remove(map(int, a))
#             if sum(a) == 0:
#                 print(a)
#                 print('Yes')
#                 t = False
#                 break
#             else:
#                 count += 1
#                 continue
#     if count == (N * (N + 1)) / 2:
#         print('No')
#         break

from itertools import combinations

for i in range(1, N+1):
    bank.append(list(combinations(storage, i)))

# print(bank)

for j in range(N):
    for k in range(len(bank[j])):
        # print(sum(bank[j][k]))
        if sum(bank[j][k]) == 0:
            print(bank[j][k])
            # break
        else:
            count += 1

standard = 0
for l in range(N):
    standard += len(bank[l])

if count == standard:
    print('No')

####################################

arr = []






