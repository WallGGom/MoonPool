import sys
sys.stdin = open('연습문제_babygin.txt', 'r')

# def babygin():

def perm(n,k):
    global res
    if k == n:
        temp = []
        count_s = 0
        count_t = 0
        for i in range(n):
            temp.append(arr[array[i]])
        for i in range(4):
            if temp[i] - temp[i+1] == -1 and temp[i+1] - temp[i+2] == -1:
                count_s += 1
            elif temp[i] - temp[i+1] == 0 and temp[i+1] - temp[i+2] == 0:
                count_t += 1
        if count_s == 1 and count_t == 1:
            res = 'Babygin'
            return
    else:
        for i in range(k,n):
            array[k], array[i] = array[i], array[k]
            perm(n, k + 1)
            array[k], array[i] = array[i], array[k]

T = int(input())

for tc in range(T):
    arr = list(map(int, input().split()))
    array = [0, 1, 2, 3, 4, 5]
    res = 'Nope'
    perm(6, 0)
    print(res)

