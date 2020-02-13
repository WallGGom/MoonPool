A = '()((()))'
B = '((()((((()()((()())((())))))'

L_g = []
R_g = []

for i in A:
    if i == '(':
        L_g.append(i)
    elif i == ')':
        R_g.append(i)
for k in range(min(len(L_g),len(R_g))):
    L_g.pop()
    R_g.pop()
if L_g == R_g:
    ans = '똑같다'
else:
    ans = '다르다'


L_g = []
R_g = []

for i in B:
    if i == '(':
        L_g.append(i)
    elif i == ')':
        R_g.append(i)
for k in range(min(len(L_g),len(R_g))):
    L_g.pop()
    R_g.pop()
if L_g == R_g:
    res = '똑같다'
else:
    res = '다르다'


print(ans, res)