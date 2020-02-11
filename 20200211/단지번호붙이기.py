import sys
sys.stdin = open('단지번호붙이기.txt','r')

danji_num = 0
danji_dic = dict()
n = int(input())

lists = [[int(block) for block in input()] for _ in range(n)]
# print(lists)

def check_around(i, j):
    """주어진 인덱스의 상하좌우를 모두 뒤져서 1이 발견될때마다 단지내 가구수를 1개씩 증가시킨다
     한 번 방문한 인덱스는 0으로 체크해서 다시 방문하지 않도록 조치한다"""
    if i != 0:
         # 상
         if lists[i-1][j] == 1:
            danji_dic[danji_num] += 1
            lists[i-1][j] = 0
            check_around(i-1, j)
    if i != n-1:
        # 하
        if lists[i+1][j] == 1:
            danji_dic[danji_num] += 1
            lists[i+1][j] = 0
            check_around(i+1, j)
    if j != 0:
        # 좌
        if lists[i][j-1] == 1:
            danji_dic[danji_num] += 1
            lists[i][j-1] = 0
            check_around(i, j-1)
    if j != n-1:
        # 우
        if lists[i][j+1] == 1:
            danji_dic[danji_num] += 1
            lists[i][j+1] = 0
            check_around(i, j+1)

for i in range(n):
    for j in range(n):
        if lists[i][j] == 1:
            danji_num += 1  # 단지를 발견했으므로 danji_num 1개 증가
            danji_dic[danji_num] = 1  # 단지별 가구수를 저장하기위해 danji_dic에 초기값 1 할당(방금 발견한 가구를 포함시킨것)
            lists[i][j] = 0  # 이미 방문한 가구는 0으로 체크해서 다시 방문하지 않도록 조치
            check_around(i, j)  # 발견한 단지의 상하좌우 전부 뒤지기

print(danji_num)
for key in sorted(danji_dic, key=lambda x: danji_dic[x]):
    print(danji_dic[key])