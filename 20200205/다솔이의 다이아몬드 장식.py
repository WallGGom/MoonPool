import sys
sys.stdin = open('다솔이의 다이아몬드 장식.txt', 'r')

T = int(input())

for tc in range(T):
    word = input()
    # print(word)
    a = ''
    b = ''
    c = ''
    d = ''
    e = ''

    for num in range(len(word)):
        if num == 0:
            a += '..#..'
            b += '.#.#.'
            c += '#.{}.#'.format(word[num])
            d += '.#.#.'
            e += '..#..'
        else:
            a += '.#..'
            b += '#.#.'
            c += '.{}.#'.format(word[num])
            d += '#.#.'
            e += '.#..'

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)




