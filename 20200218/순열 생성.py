def perm(n,k):

    if k == n:
        for i in range(n):
            print(data[array[i]], end=' ')
        print()
    else:
        for i in range(k,n):
            array[k], array[i] = array[i], array[k]
            perm(n, k + 1)
            array[k], array[i] = array[i], array[k]

data = [3, 6, 9]
array = [0, 1, 2]
perm(3,0)