import sys
sys.stdin = open('보충학습과 평균.txt', 'r')

T = int(input())
for tc in range(T):
    score = list(map(int, input().split()))
    # print(score)
    for idx, sco in enumerate(score):
        if sco < 40:
            score[idx] = 40
    # print(score)
    print('#{} {}'.format(tc+1, sum(score)//5))
