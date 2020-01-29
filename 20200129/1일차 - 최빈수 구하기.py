import sys
sys.stdin = open('1일차 - 최빈수 구하기.txt', 'r')

T = int(input())
score = [0]*101

for tc in range(T):
    N = int(input())
    data = list(map(int, input().split())) #공백으로 구분해서 int로 받아서 list를 만든다.
    for i in range(1000):
        score[100-data[i]] += 1
        # 케이스3에서는 최빈수가 77, 79점이 동일 갯수인데, 이중 큰수를 출력해야함
    a = 100-score.index(max(score))
    print('#{} {}'.format(N, a))
    score = [0] * 101
