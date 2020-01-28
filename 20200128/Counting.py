a = [0, 3, 1, 5, 1, 2, 4, 1]
b = [0] * int(max(a)+1)
c = [0] * len(a)

for i in range(len(a)): # 카운팅
    b[a[i]] += 1
print(b)

for j in range(len(b)-1): # 누적
    b[j+1] = b[j] + b[j+1]
print(b)

for k in range(len(a)-1, -1, -1): # 자기자리 찾아가기
    c[b[a[k]]-1] = a[k]
    b[a[k]] -= 1
print(c)


