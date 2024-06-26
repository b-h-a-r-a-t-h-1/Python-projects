'''power method :
        it is used to solve eigen value problems .in some applications,
        it is required to compute numerically largest eigen value 
        and its corresponding eigen vector.
        it is also known as Rayleigh's power method.'''

n=int(input('enter number of rows of the given square matrix:'))
# =============================================================================
# Given matrix:
# =============================================================================
lst=[]
for i in range(n):
    lst1=[]
    for j in range(n):
        print('enter',i,j,'th element of the given matrix:')
        a=float(input(' '))
        lst1.append(a)
    lst.append(lst1)
print(lst)
A=lst.copy()

# =============================================================================
# initial approximation of largest eigen vector:
# =============================================================================
lst2=[]
for i in range(n):
    if i==0:
        lst2.append(1)
    else:
        lst2.append(0)
print(lst2)
X=lst2.copy()
'''process  is continue till the eigen value of previous iteration 
is equal to current iteration'''
s=0
while True:
    for i in range(n):
        a=0
        for j in range(n):
            b=A[i][j]
            c=lst2[j]
            d=b*c
            a+=d
        X[i]=a
    e=0
# =============================================================================
#     Finding eigen value and eigen vector of current iteration:
# =============================================================================
    for i in  range(n):
        if i==0:
            e=X[0]
        g=X[i]
        c=g/e
        X[i]=c
# =============================================================================
# condition to exit the iteration:
# =============================================================================
    if e==s:
# =============================================================================
# formating the eigen value upto two decimal places:
# =============================================================================
        print('Largest eigen value =','{:.2f}'.format(e))
        break
    else:
        s=e
        lst2=X.copy()
# =============================================================================
# formating the values upto 2 decimal places of eigen vector: 
# =============================================================================
for i in range(n):
    a=X[i]
    b='{:.2f}'.format(a)
    c=float(b)
    X[i]=c
print('Eigen vector corresponding to largest eigen value is \n',X)
# =============================================================================
# Program ends
# =============================================================================