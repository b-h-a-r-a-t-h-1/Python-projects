'''percentage calculation:
    useful to present the classes'''

def percent(a,b):
    z=(b/a)*100
    return z
def per():
    z=percent(x,y)
    print('absent percentage=',round(z,2))
    print('present percentage=',round((100-z),2))
    
x=int(input('enter total number of classes:'))
y=int(input('enter number of classes you absent:'))
per()
p,s=100,0
while p>26:
    p=percent(x,y)
    s+=1
    x+=1
print()
print('present percentage=',round(100-p,2))
print('total class to be present without absent:\n',s-1)
