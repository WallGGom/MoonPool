import sys
sys.stdin = open('통역사 성경이.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    word = str(input())
    W = word

    goodoo = '?!.'

    # print(word)

    ind = [0]
    for _ in range(len(word)):
        if word[_] == '?':
            ind.append(_)
        elif word[_] == '!':
            ind.append(_)
        elif word[_] == '.':
            ind.append(_)

    table = str.maketrans('?!.', '   ')
    new_word = word.translate(table)
    # print(new_word)


    sentense = []
    for i in range(len(ind)-1):
        sentense.append(new_word[ind[i]:ind[i+1]].strip())
    # print(sentense)

    result = []
    for S in range(len(sentense)):
        result.append(list(sentense[S].split()))
    # print(result)


    res = []
    for y in result:
        count = 0
        for x in y:
            if x[0].isupper():
                count += 1
                for j in range(1, len(x)):
                    if x[j].isupper():
                        count -= 1
                        break
                    elif x[j].isdecimal():
                        count -= 1
                        break
        res.append(count)

    # print(res)
    yam = ''
    for y in res:
        yam += str(y) + ' '

    print('#{} {}'.format(tc+1, yam))












