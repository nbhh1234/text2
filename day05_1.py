#_*_ -conding:utf8-
x=raw_input('ddd-dd-dddd>>')
print x
a=x[0:3]
e=x[3:4]
b=x[4:6]
f=x[6:7]
c=x[7:]

if a.isdigit()==True and b.isdigit()==True and c.isdigit()==True and e=='-' and f=='-':
    print 'Valid SSN'
else:
    print 'Invalid SSN'
    
