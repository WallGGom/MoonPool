def printArray():
    for i in range(len(arr)):
        print('%3d' % arr[i], end=' ')
    print()

def partition(a, l, r):
    p = a[l]
    i = l
    j = r

    while i < j:
        while a[i] <= p:
            i += 1
            if (i == r):
                break
        while a[j] >= p:
            j -= 1
            if (j == l):
                break
        if i < j:
            a[i], a[j] = a[j], a[i]

    a[l], a[j] = a[j], a[l]
    return j

def quicksort(a, low, high):
    if low < high:
        s = partition(a, low, high)
        quicksort(a, low, s-1)
        quicksort(a, s+1, high)

arr = [11, 45, 22, 81, 23,34, 99, 22, 17, 8]

printArray()
quicksort(arr, 0, len(arr)-1)
printArray()