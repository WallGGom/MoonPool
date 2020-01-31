# def pick_and_sum(word):
#     for char in word:
#         if char.isalpha():
#             word = word.replace(char, ' ')
#     picks = list(map(int, word.split()))
#     return sum(picks)


def pick_and_sum(word):
    result = 0
    num = ''

    for w in word:
        if w.isdecimal():
            num += w
        elif num:
            result += int(num)
            num = ''

    return result






print(pick_and_sum('The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog'))