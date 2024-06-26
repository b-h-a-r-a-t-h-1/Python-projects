''' decomposition method:'''

#equation matrix A:
n=int(input("enter number of equations:"))
lst=[]
for i in range(1,n+1):
    lst1=[]
    print('enter coefficient of equation',i)
    for j in range(n+1):
        a=float(input('enter coefficients'))
        lst1.append(a)
    lst.append(lst1)
print(lst)

l=[]
r=[]
#LHS
for i in range(n):
    p=[]
    for j in range(n):
        e=lst[i][j]
        p.append(e)
    l.append(p)
lst3=l.copy()
print(l)
#RHS:
for i in range(n):
    for j in [1]:
        e=lst[i][n]
        r.append(e)
print(r)
lst4=r.copy()
#lower triangular Matrix:
L=[]
for i in range(n):
    lst1=[]
    for j in range(n):
        if i==j:
            lst1.append(1)
        elif i>j:
            lst1.append(2)
        else:
            lst1.append(0)
    L.append(lst1)
print('lower',L)
#Upper triangular Matrix:
U=[]
for i in range(n):
    lst1=[]
    for j in range(n):
        if i<=j:
            lst1.append(1)
        else:
            lst1.append(0)
    U.append(lst1)
print('upper',U)

