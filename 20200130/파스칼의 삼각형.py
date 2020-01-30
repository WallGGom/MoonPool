import sys
sys.stdin = open('파스칼의 삼각형.txt', 'r')

N = int(input())
for tc in range(N):
    prev_line = [1]
    print('#{}'.format(tc + 1))
    print(1)
    n = int(input())
    for i in range(n - 1):
        present_line = [1]
        for j in range(1, len(prev_line)):
            present_line.append(prev_line[j - 1] + prev_line[j])
        present_line.append(1)

        print(' '.join(map(str, present_line)))
        prev_line = present_line
