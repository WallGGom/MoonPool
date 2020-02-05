import sys
sys.stdin = open('영준이의 카드 카운팅.txt', 'r')

T = int(input())


for tc in range(T):
    card = input()
    dic = {'S': 13, 'D': 13, 'H': 13, 'C': 13}
    t = True

    for i in range(0,len(card),3):
        for j in range(i+3, len(card),3):
            if card[i:i+3] == card[j:j+3]:
                t = False
                break
        if card[i] == 'S':
            dic['S'] -= 1
        elif card[i] == 'D':
            dic['D'] -= 1
        elif card[i] == 'H':
            dic['H'] -= 1
        elif card[i] == 'C':
            dic['C'] -= 1
    if t:
        res = '{} {} {} {}'.format(dic['S'], dic['D'], dic['H'], dic['C'])
    else:
        res = 'ERROR'

    print('#{} {}'.format(tc + 1, res))