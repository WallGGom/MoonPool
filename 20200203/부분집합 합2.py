# import random

N = int(input())

array = [0]*N

# for i in range(N):
#     array[i] = random.choice(range(-(2*N),(2*N)+1))

for i in range(N):
    array[i] = i + 1

arr = sorted(array)
bank = []
storage = []
cho = []

if cho:
    start = arr.index(cho[-1]) + 1
else:
    start = 0

for r in range(1, N+1):
    for nxt in range(start, len(arr)):
        cho.append(arr[nxt])
        if len(cho) == r:
            # print(chosen)
            bank.append(cho)
        cho.remove(arr[nxt])
    storage.append(bank)

print(storage)






# print(bank)



# storage = []
# storage.append(combination(array, 2))
# print(storage)


