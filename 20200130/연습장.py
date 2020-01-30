# word = [['KO'],['RE']]
#
# print(word[0][0])

n = 4
prev_line = [1]
print(1)
for i in range(n - 1):
    present_line = [1]
    for j in range(1, len(prev_line)):
        present_line.append(prev_line[j - 1] + prev_line[j])
    present_line.append(1)

    print(' '.join(map(str, present_line)))
    prev_line = present_line
























# num = -0.0



# if type(num) is complex:
#         a = ((num.real**2) + (num.imag**2))**0.5
# elif type(num) is float:
#     if num >= 0.0:
#         a = num
#     elif num == -0.0:
#         a = -num
#     elif num < 0.0:
#         a = -num
# elif type(num) is int:
#     if num >= 0.0:
#         a = num
#     elif num < 0.0:
#         a = -num
#
# print(a)

# a = [[], 2, 5, '6']
# count = 0
# for i in a:
#     if bool(i) == True:
#         count += 1
#     else:
#         continue
#
# if count == len(a):
#     ans = 'True'
# elif count == 0:
#     ans = 'True'
# else:
#     ans = 'False'
#
# print(ans)

# def my_all(something):
#     count = 0
#     for i in something:
#         if bool(i) == True:
#             count += 1
#         else:
#             continue
#
#     if count == len(something):
#         ans = 'True'
#     elif count == 0:
#         ans = 'True'
#     else:
#         ans = 'False'
#     return ans
#
# print(my_all([[], 2, 5, '6']))

























