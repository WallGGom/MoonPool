def printset(n):
    temp = 0
    bank = []
    for i in range(n):
        if A[i] == 1:
            temp += data[i]
            bank.append(str(data[i]))
        if temp > 10:
            break
    if temp == 10:
        print(' '.join(bank))

def powerset(n, k):
    if n == k:
        printset(n)
    else:
        A[k] = 1
        powerset(n, k + 1)
        A[k] = 0
        powerset(n, k + 1)

N = 10
A = [0 for _ in range(N)]
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

powerset(N, 0)