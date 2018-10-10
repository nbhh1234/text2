#_*_ -coding:utf8
'''
class ep2:
    def __init__(self):
        self.num=10
        print ('wqqqq')
    def num_2(self):
        self.num=self.num ** 2
        print self.num
    def num_3(self):
        self.num=self.num**3
        print self.num
if __name__ == '__main__':
    wang=ep2()
    wang.num_2()
    wang.num_3()
'''
'''
#EP1
class Rectangle:
    def __init__(self,width,heightd):
        self.width=width
        self.heightd=heightd
    def getArea(self):
        mianji= self.width * self.heightd
        print mianji
    def getPerimeter(self):
        zhou=(self.width+self.heightd)*2
        print zhou
Rec=Rectangle(4,40)
Rec1=Rectangle(3.5,35.7)

Rec.getArea()
Rec.getPerimeter()
Rec1.getArea()
Rec1.getPerimeter()
'''
'''
#EP2
class Account:
    def __init__ (self,name,balance,air):
        self.__id=name
        self.__balance=balance
        self.__air=air/100
    def gmir(self):
        self.mir=self.__air/12
    def gmi(self):
        self.mi=self.__balance*self.mir
    def withdraw(self,money):
        self.__balance=self.__balance-money
        print self.__id,self.__balance,self.mir,self.mi
    def deposit(self,money1):
       self.__balance=self.__balance+money1
       self.mi=self.__balance*self.mir
       print self.__id,self.__balance,self.mir,self.mi
ac=Account(1122,20000,4.5)
ac.gmir()
ac.gmi()
ac.withdraw(2500)
ac.deposit(3000)

'''
'''
import math
class RegularPolygon:
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__n=n
        self.__side=side
        self.__x=x
        self.__y=y
    def getPerimeter(self):
        zhou=self.__n*self.__side
        print zhou
    def getArea(self):
        mj=(self.__n*self.__side**2)/(4*math.tan(math.pi/self.__n))
        print mj
re1=RegularPolygon()
re1.getPerimeter()
re1.getArea()
re2=RegularPolygon(6,4)
re2.getPerimeter()
re2.getArea()
re3=RegularPolygon(10,4,5.6,7.8)
re3.getPerimeter()
re3.getArea()

'''
'''

#EP6
import math
class LinEq:
    def __init__(self,x1,y1,x2,y2):
        self.__x1=x1
        self.__y1=y1
        self.__x2=x2
        self.__y2=y2
    def qe(self):
       
'''
'''
#EP4
slow=1
medium=2
fast=3
class Fan:
    def __init__(self,speed=slow,on=False,radius=5,color='blue'):
        self.__speed=speed
        self.__on=on
        self.__radius=radius
        self.__color=color
    def mr(self):
        print self.__speed,self.__on,self.__radius,self.__color
fa1=Fan(fast,True,10,'yellow')
fa2=Fan(medium,False,5,'blue')
fa1.mr()
fa2.mr()
'''
'''
#EP5
class Leq():
    def __init__(s,a,b,c,d,e,f):
        s.__a=a
        s.__b=b
        s.__c=c
        s.__d=d
        s.__e=e
        s.__f=f
    def isS(s):
        if (s.__a*s.__d)-(s.__b*s.__c)!=0:
            return True
            
    def getX(s):
        x=((s.__e*s.__d)-(s.__b*s.__f))/((s.__a*s.__d)-(s.__b*s.__c))
        print x
    def getY(s):
        y=((s.__a*s.__f)*(s.__e*s.__c))/((s.__a*s.__d)-(s.__b*s.__c))
        print y
a,b,c,d,e,f=input('>>')
L=Leq(a,b,c,d,e,f)
L.isS()
if(L.isS()==True):
    L.getX()
    L.getY()
else:
    print'ci fang cheng wu jie'
'''
'''
#EP6
class Leq():
    def __init__ (s,x1,y1,x2,y2):
        s.__x1=x1
        s.__y1=y1
        s.__x2=x2
        s.__y2=y2
    def fc(s):
        k=(y2-y1)/(x2-x1)
        b=(x2*y1-y2*x1)/(x2-x1)


'''
'''
url1='http://www.baidu.com/?page='
url2='?wd=xiaopangzi'
for i in range (1,1000):
    str_i=str(i)
    print (str_i).join((url1,url2))

'''
'''
A2=[1,1,1,1,1,2,2,2,2,3,4]
A3=[]
for i in A2:
    if i not in A3:
        A3.append(i)
print A3
'''
'''
a4=[['liuyanyun',22,['360',100]],['jingjing',12,['baidu',1]],['taotao',-1,['google',0]]]
a4.sort(key=lambda x:x[2][1])
print a4
'''

