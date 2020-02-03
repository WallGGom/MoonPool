# bit = [0, 0, 0, 0]
#
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit)



def combination(arr, r):
    # 1.
    arr = sorted(arr)

    # 2.
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return

    	# 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()
    generate([])

combination('ABCDE', 2)