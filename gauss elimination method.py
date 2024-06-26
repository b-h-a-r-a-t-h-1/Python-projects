'''GAUSS ELIMINATION METHOD:
 In this method,the unknouns are eliminated successively and the system is 
reduced to upper triangular system from which the unknowns are found by 
back substitution.'''

# =============================================================================
# defining functions for two variables:
# =============================================================================
def bvalue():
    l=lst[1][2]
    m=lst[1][1]
    return l/m
def avalue(b):
    l=lst[0][2]-(b*lst[0][1])
    m=lst[0][0]
    return l/m
# =============================================================================
# defining functions for three variables:
# =============================================================================
def zvalue():
    l=lst[2][3]
    m=lst[2][2]
    return l/m
def yvalue(z):
    l=lst[1][3]-(z*lst[1][2])
    m=lst[1][1]
    return l/m
def xvalue(z,y):
    l=lst[0][3]-(z*lst[0][2])-(y*lst[0][1])
    m=lst[0][0]
    return l/m
# =============================================================================
# defining functions for three variables:
# =============================================================================
def x1value(y,z,u):
    a=lst[0][3]-(y*lst[0][1])-(z*lst[0][2])-(u*lst[0][3])
    b=lst[0][0]
    return a/b
def y1value(z,u):
    a=lst[1][4]-(z*lst[1][2])-(u*lst[1][3])
    b=lst[1][1]
    return a/b
def z1value(u):
    a=lst[2][4]-(u*lst[2][3])
    b=lst[2][2]
    return a/b
def uvalue():
    a=lst[3][4]
    b=lst[3][3]
    return a/b
# =============================================================================
# equation matrix A:
# =============================================================================
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
# =============================================================================
# variables matrix X:
# =============================================================================
'''X=[]
for i in range(n):
    print('enter',i+1,'st variable')
    x=input('')
    X.append(x)
print(X)'''
# =============================================================================
# finding row echlon form of matrix A:
# =============================================================================
s,a=0,0
x=list(range(1,n))
print(x)
y=list(range(n+1))
print(y)
for i in x:
    b=lst[i-1][s]
    c=i
    while c!=n:
        d=lst[c][s]
        a=b/d
        for j in y:
            e=a*lst[c][j]
            f=lst[i-1][j]
            g=e-f
            lst[c][j]=g
        c+=1
    a=0
    s+=1
print(lst)
lst1=lst.copy()
# =============================================================================
# formatting answers to 2 decimal places:
# =============================================================================
if n==2:
    b=bvalue()
    a=avalue(b)
    print('x=','{:.2f}'.format(a))
    print('y=','{:.2f}'.format(b))
if n==3:
    z=zvalue()
    y=yvalue(z)
    x=xvalue(y, z)
    print('x=','{:.2f}'.format(x))
    print('y=','{:.2f}'.format(y))
    print('z=','{:.2f}'.format(z))
if n==4:
    u=uvalue()
    z1=z1value(u)
    y1=y1value(z1, u)
    x1=x1value(y1, z1, u)
    print('x=','{:.2f}'.format(x1))
    print('y=','{:.2f}'.format(y1))
    print('z=','{:.2f}'.format(z1))
    print('u=','{:.2f}'.format(u))
    
# =============================================================================
# program ends:
# =============================================================================


#splitting LHS and RHS
#LHS:
'''l=[]
r=[]
for i in range(n):
    p=[]
    for j in range(n):
        e=lst1[i][j]
        p.append(e)
    l.append(p)
lst3=l.copy()
print(l)
#RHS:
for i in range(n):
    for j in [1]:
        e=lst1[i][n]
        r.append(e)
print(r)
lst4=r.copy()'''

'''x,a=n-1,0
mth=list(range(-1,-1*n,-1))
nth=list(range(-1,(-1*n)-2,-1))
for i in mth:
    b=lst[i][n]
    #print(b)
    h=i
    while h!=-1*n:
        d=lst[i][x]
        #print(d)
        a=b/d
        print(a)
        for j in nth:
            e=a*lst[h-1][i-1]
            f=lst[h-1][n]
            g=f-e
            lst[h-1][n]=g
        h=h-1
    x=x-1
    a=0'''
            