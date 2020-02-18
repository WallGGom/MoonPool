import sys
sys.stdin = open('01 Knapsack.txt', 'r')

def getmax(index, capacity):

    if index == N:
        return 0
    unselected = getmax(index + 1, capacity)
    selected = 0
    if capacity >= volume[index]:
        selected = getmax(index + 1, capacity-volume[index]) + value[index]
    return max(unselected, selected)

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    volume = []
    value = []

    for _ in range(N):
        V, C = map(int, input().split())
        volume.append(V)
        value.append(C)

    print('#{} {}'.format(tc+1, getmax(0, K)))

