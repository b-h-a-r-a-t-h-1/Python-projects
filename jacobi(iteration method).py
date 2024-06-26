''''jacobi's iteration method:
    iteration method are used for system of linear equations in which 
    the coefficients of leading diagonal are large compared to others.
    
    In this method the initial approximation for solving the equations are
    values of variables are zero.,i.e for linear equation with 
    three variable(x,y,z) are x=y=z=0. 
    
    iteration is continued till the values of variables in previous iteration 
    and current iteration are approximately equal'''

# =============================================================================
# defining functions for linear Eqn with two variables:
# =============================================================================
def avalue(y):
    for i in [0]:
        c=lst[0][0]
        d=lst[0][2]-(y*lst[0][1])
        a=d/c
        return a
def bvalue(x):
    for i in [1]:
        c=lst[1][1]
        d=lst[1][2]-(x*lst[1][0])
        b=d/c
        return b    
# =============================================================================
# defining functions for linear Eqn with three variables:
# =============================================================================
def xvalue(y,z):
    for i in [0]:
        c=lst[0][0]
        d=lst[0][3]-(y*lst[0][1])-(z*lst[0][2])
        e=d/c
        return e
def yvalue(x,z):
    for i in [1]:
        c=lst[1][1]
        d=lst[1][3]-(x*lst[1][0])-(z*lst[1][2])
        f=d/c
        return f
def zvalue(x,y):
    for i in [2]:
        c=lst[2][2]
        d=lst[2][3]-(x*lst[2][0])-(y*lst[2][1])
        g=d/c
        return g
# =============================================================================
# defining functions for linear Eqn with four variables:
# =============================================================================
def x1value(y,z,u):
    for i in [0]:
        c=lst[0][0]
        d=lst[0][4]-(y*lst[0][1])-(z*lst[0][2])-(u*lst[0][3])
        x1=d/c
        return x1
def y1value(x,z,u):
    for i in [1]:
        c=lst[1][1]
        d=lst[1][4]-(x*lst[1][0])-(z*lst[1][2])-(u*lst[1][3])
        y1=d/c
        return y1
def z1value(x,y,u):
    for i in [2]:
        c=lst[2][2]
        d=lst[2][4]-(x*lst[2][0])-(y*lst[2][1])-(u*lst[2][3])
        z1=d/c
        return z1
def uvalue(x,y,z):
    for i in [3]:
        c=lst[3][3]
        d=lst[3][4]-(x*lst[3][0])-(y*lst[3][1])-(z*lst[3][2])
        z1=d/c
        return z1
n=int(input("enter number of equations:"))

'''solution for linear equation with two variables:'''
# =============================================================================
# equation matrix
# =============================================================================
if n==2:
    lst=[]
    for i in range(1,n+1):
        lst1=[]
        print('enter coefficient of equation',i)
        for j in range(n+1):
            a=float(input('enter coefficients'))
            lst1.append(a)
        lst.append(lst1)
    print()
# =============================================================================
# initial approximation:
# =============================================================================
    x,y,s=0,0,0
    a=avalue(y)
    b=bvalue(x)
    while True:
        if a==x or b==y:
            print('x=','{:.2f}'.format(a))
            print('y=','{:.2f}'.format(b))
            break
        else:
            x=a
            y=b
            a=avalue(y)
            b=bvalue(x)
        s+=1
    print('number of iteration=',s)
    
'''solution for linear equation with three variables:'''
# =============================================================================
# equation matrix:
# =============================================================================
if n==3:
    lst=[]
    for i in range(1,n+1):
        lst1=[]
        print('enter coefficient of equation',i)
        for j in range(n+1):
            a=float(input('enter coefficients'))
            lst1.append(a)
        lst.append(lst1)
    print()
# =============================================================================
# initial approximation:
# =============================================================================
    x,y,z,s=0,0,0,0
    l=xvalue(y,z)
    m=yvalue(x,z)
    n=zvalue(x,y)
    while True:
        if l==x or m==y or n==z:
            print('x=','{:.2f}'.format(l))
            print('y=','{:.2f}'.format(m))
            print('z=','{:.2f}'.format(n))
            break
        else:
            x=l
            y=m
            z=n
            l=xvalue(y, z)
            m=yvalue(x, z)
            n=zvalue(x, y)
        s+=1
    print('number of iteration=',s)
    
'''solution for linear equation with four variables:'''
# =============================================================================
# equation matrix:    
# =============================================================================
if n==4:
    lst=[]
    for i in range(1,n+1):
        lst1=[]
        print('enter coefficient of equation',i)
        for j in range(n+1):
            a=float(input('enter coefficients'))
            lst1.append(a)
        lst.append(lst1)
    print()
# =============================================================================
# initial approximation:
# =============================================================================
    x,y,z,u,s=0,0,0,0,0
    x1=x1value(y, z, u)
    y1=y1value(x, z, u)
    z1=z1value(x, y, u)
    v=uvalue(x, y, z)
    while True:
        if x1==x or y1==y or z1==z or v==u:
            print('x=','{:.2f}'.format(x1))
            print('y=','{:.2f}'.format(y1))
            print('z=','{:.2f}'.format(z1))
            print('u=','{:.2f}'.format(v))
            break
        else:
            x=x1
            y=y1
            z=z1
            u=v
            x1=x1value(y, z, u)
            y1=y1value(x, z, u)
            z1=z1value(x, y, u)
            v=uvalue(x, y, z)
        s+=1
    print('number of iteration=',s)
 # =============================================================================
 # Program ends
 # =============================================================================      