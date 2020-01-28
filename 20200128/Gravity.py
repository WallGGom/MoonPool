# Gravity.py
# import random
# data = random.sample(list(range(0,9)), 9)
# print(data)
data = [7, 4, 2, 0, 0, 6, 0, 7, 0]

nuM = -1
for p in range(len(data)):
    if data[p] == max(data):
        start = p
        break
Height = len(data) - (start + 1)

for i in range(len(data)):
    if data[i] == max(data):
        nuM += 1

maxHeight = Height - nuM

print(maxHeight)



# for i in range(len(data)):
#     for j in range(len(data)):
#         if data[i] == M:





#            maxHeight += 1
#Height = len(data) - int(maxHeight/number())
#print(Height)


