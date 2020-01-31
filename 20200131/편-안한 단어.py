# 왼손: q, w, e, r, t, a, s, s, d, f, g, z, x, c, v, b
# 오른손: y, u, i, o, p, h, j, k, l, n, m

def comfortable_word(word):
    left = ['q', 'w', 'e', 'r', 't', 'a', 's', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
    right = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']
    count = 0

    for i in range(len(word)-1):
        if word[i] in left and word[i+1] in right:
            count += 1
        elif word[i] in right and word[i+1] in left:
            count += 1

    if count == len(word)-1:
        return 'True'
    else:
        return 'False'

print(comfortable_word('qywu'))
print(comfortable_word('apple'))