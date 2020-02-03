N = 10

datalist = list(map(int,input().split()))   # 10개의 수를 입력받음
upper = 1<<N
flag = False
for i in range(upper) :
    sum = 0;
    for j in range(N) :
        if i&(1<<j) : sum += datalist[j]
    if i and sum==0 : flag = True; break

print("Exist" if flag else "Not Exist")