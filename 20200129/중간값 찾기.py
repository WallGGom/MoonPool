import sys
sys.stdin = open('중간값 찾기.txt', 'r')

T = int(input())
data = list(map(int, input().split()))  # 공백으로 구분해서 int로 받아서 list를 만든다.

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] > data[j]:
            data[i], data[j] = data[j], data[i]

print(data[T//2])

