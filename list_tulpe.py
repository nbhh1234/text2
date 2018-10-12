'''
#EP2
x=input('x>>')
y=input('y>>')
j=0
if len(x)>len(y):
    for i in y:
        if i in x:
            j+=1
            if j==len(y):
                print('y存在于x')
        else:
            j+=1
            if j==len(x):
                print ('y不存在于x')

elif len(x)<len(y):
    for i in x:
        if i in y:
            j+=1
            if j==len(x):
                print('x存在于y')
        else:
            j+=1
            if j==len(x):
                print ('x不存在于y')
else:
    for i in x:
        if i in y:
            j+=1
            if j==len(x):
                print('x与y元素相同')
        else:
            j+=1
            if j==len(x):
                print ('x与y元素不同')
#EP3 
#_*_ -coding:utf8-
a=input('>>')
b=len(a)
j=0
if b>=8 and a.isalnum()==True:
    for i in range (0,len(a)):
        if a[i].isdigit()==True:
            j+=1
            if j>=2:
                print ('valid password')
                break
            else:
                print ('invalid password1')
    else:
        print ('invalid password2')
else:
    print ('invalid password')
#EP4
#_*_ -conding:utf8-
a=input('>>')
b=len(a)
def conuntLetters(s):
    j=0
    for i in range (0,b):
        if a[i].isalpha()==True:
            j+=1
    print (j)
conuntLetters(a)
#EP5
#_*_ -conding:utf8-
a=input('number>>')
b=len(a)
c=[]
for i in range (b):
    if a[i]=='1':
        c.append('1')
    elif a[i]=='2' or a[i]=='a' or a[i]=='b' or a[i]=='c' or a[i]=='A' or a[i]=='B' or a[i]=='C':
        c.append('2')
    elif a[i]=='3' or a[i]=='d' or a[i]=='e' or a[i]=='f' or a[i]=='D' or a[i]=='E' or a[i]=='F':
        c.append('3')
    elif a[i]=='4' or a[i]=='g' or a[i]=='h' or a[i]=='i' or a[i]=='G' or a[i]=='H' or a[i]=='I':
        c.append('4')
    elif a[i]=='5' or a[i]=='j' or a[i]=='k' or a[i]=='l' or a[i]=='J' or a[i]=='K' or a[i]=='L':
        c.append('5')
    elif a[i]=='6' or a[i]=='m' or a[i]=='n' or a[i]=='o' or a[i]=='M' or a[i]=='N' or a[i]=='O':
        c.append('6')
    elif a[i]=='7' or a[i]=='p' or a[i]=='q' or a[i]=='r' or a[i]=='s' or a[i]=='P' or a[i]=='Q' or a[i]=='R' or a[i]=='S':
        c.append('7')
    elif a[i]=='8' or a[i]=='t' or a[i]=='u' or a[i]=='v' or a[i]=='T' or a[i]=='U' or a[i]=='V':
        c.append('8')
    elif a[i]=='9' or a[i]=='w' or a[i]=='x' or a[i]=='y' or a[i]=='z' or a[i]=='W' or a[i]=='X'or a[i]=='Y' or a[i]=='Z':
        c.append('9')
    elif a[i]=='0':
        c.append('0')
    elif a[i]=='-':
        c.append('-')
    elif a[i]=='*':
        c.append('*')
    elif a[i]=='#':
        c.append('#')
b=[str(i) for i in c]
a=''.join(b)
print (a)
#EP6
a=input('>>')
def reverse(s):
    b=reversed(s)
    c=[str(i) for i in b]
    d=''.join(c)
    print (d)
reverse(a)
    
#EP8
#_*_ -conding:utf8-
a=input('>>')
b=len(a)
sum1=0
for i in range(0,b):
    if i==0 or i==2 or i==4 or i==6 or i==8 or i==10:
        c=int(a[i])
        sum1=sum1+c
    if i==1 or i==3 or i==5 or i==7 or i==9 or i==11:
        c=int(a[i])
        sum1=sum1+c*3
s=10-sum1%10
if s<10:
    str_s=str(s)
    print (a+str_s)
else:
    s=s%10
    str_s=str(s)
    print (a+str_s)

#EP2_1
a,b,c,d=(eval(j) for j in input('>>').split(' '))
best=max(a,b,c,d)
for i in range (0,4):
    if x[i]>=best-10:
        print ('{} is A'.format(x[i]))
    elif x[i]>=best-20:
         print ('{} is B'.format(x[i]))
    elif x[i]>=best-30:
         print ('{} is C'.format(x[i]))
    elif x[i]>=best-40:
         print ('{} is D'.format(x[i]))
    else:
        print('{} is F'.format(x[i]))
            
#EP2_2
a=list(input('>>').split(' '))
a.reverse()
print (a)


#EP2_3
a=list(input('>>').split(' '))
b=len(a)
x=list(set(a))
#print (x)
for i in range (0,len(x)):
    k=a.count(x[i])
    print ('{} occurs {} tims'.format(x[i],k))

    
#EP2_4
a=list(input('>>').split(' '))
b=[int(i) for i in a]
sun=0
k=0
j=0
for i in b:
    sun+=i
x=sun/len(b)
for i in range (len(b)):
    if b[i]>=x:
        k+=1
    else:
        j+=1
print ('{} 个高于等于平均分'.format(k))
print ('{} 个低于平均分'.format(j))
    


#EP2_5
import random
a=[]
c=[]
for i in range (0,1000):
    i=random.randint(0,9)
    a.append(i)
b=[0,1,2,3,4,5,6,7,8,9]
for j in range(0,10):
    k=a.count(b[j])
    c.append(k)
print (c)
    
    
