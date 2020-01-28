a = input()
t1 = False
t2 = False
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            for k in range(j+1, len(a)):
                if a[k] == a[i] and a[k] == a[j]:
                    t1 = True
for x in range(len(a)):
    for y in range(x+1, len(a)):
        if int(a[x]) - int(a[y]) == 1:
            for z in range(y+1, len(a)):
                if int(a[z]) - int(a[x]) == 1:
                    t2 = True
                if int(a[y]) - int(a[z]) == 1:
                    t2 = True
        if int(a[x]) - int(a[y]) == -1:
            for z in range(y+1, len(a)):
                if int(a[z]) - int(a[x]) == -1:
                    t2 = True
                if int(a[y]) - int(a[z]) == -1:
                    t2 = True

        if int(a[x]) - int(a[y]) == 2:
            for z in range(y+1, len(a)):
                if int(a[z]) - int(a[y]) == 1:
                    t2 = True
        if int(a[x]) - int(a[y]) == -2:
            for z in range(y+1, len(a)):
                if int(a[z]) - int(a[x]) == 1:
                    t2 = True

if t1:
    print('Triple')
if t2:
    print('Run')
if t1 and t2:
    print('Baby-gin')