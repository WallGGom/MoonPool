a = [2, 55, 7, 78, 12, 42, 123, 15, 34, 76, 49, 6]

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a)


# def BubleSort(a): # 예시
#     for i in range(len(a)-1, 0, -1):
#         for j in range(0, i):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
