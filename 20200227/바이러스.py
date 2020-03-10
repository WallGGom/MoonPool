import sys
sys.stdin = open('바이러스.txt', 'r')

def rusrus(com):
    check = []
    temp = []
    temp.append(1)

    while temp:
        node = temp.pop()
        if node not in check:
            check.append(node)
            temp += com[node]
    return len(check)


N = int(input())
pair = int(input())
com = [[] for i in range(N+1)]

for _ in range(pair):
    y, x = map(int, input().split())
    com[y].append(x)
    com[x].append(y)
# print(com)
print(rusrus(com)-1)

