'''
인풋 값
6
2 0102 80
2 0106 90
2 0104 85
1 0103 80
1 0101 90
1 0105 85
'''


# group은 0번 열
# score는 2번 열

def selSort(a) :
    for i in range(len(a) - 1) :
        min = i
        for j in range(i+1, len(a)) :
            # 그룹번호 우선, 만약 그룹번호가 같다면 score를 기준으로 배열
            if a[min][0] > a[j][0] or a[min][0] == a[j][0] and a[min][2] > a[j][2]: min = j
        a[i], a[min] = a[min], a[i]

# 1차원 정렬

# datalist = list(map(int, input().split()))

# datalist = list(input().split())

# print(datalist)
#
# selSort(datalist)
#
# print(datalist)

# 2차원 정렬

N = int(input())
datamap = [list(map(int, input().split())) for _ in range(N)]
# print(datamap)

for i in range(len(datamap)):
    print(datamap[i])

print('')
# selSort(datamap)
# datamap.sort(key = lambda x : x[1])  # x가 1번 열이라는 것을 명시

datamap.sort(key = lambda x : x[2])
datamap.sort(key = lambda x : x[0])  # 이 경우는 순서가 중요하다.
# 조건이 그룹 순으로 정렬하되, 그룹이 같은 경우 점수를 기준으로 정렬하는 것이기 때문이다.
# 점수를 기준으로 정렬되어 있는 리스트, 이 상태에서 다음 명령어 '그룹'으로 정렬을 할 때
# 아예 그룹을 기준으로 정렬하는 것이 아니라
# 이 경우에는 점수를 기준으로 정렬을 한 번 했기 때문에 감안해서 정렬된다.

# 파이썬의 경우만 이전에 정렬된 명령어를 생각하면서 정렬해준다


for i in range(len(datamap)) :
    print(datamap[i])