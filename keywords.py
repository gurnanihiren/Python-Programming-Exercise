

print('_______________________')
print('Keywords in Python')
import keyword
print(f'List of All Keywords in Python are {keyword.kwlist}')

count=0
for i in keyword.kwlist:
    count=count+1
    
print(f'Total no of Keywords in Python are {count}')

print('Boolean True and Boolean False Keyword in Python')
x=2
print(x == 2)
y=3
print(y == 3)
z=5
print(z!=5)
print(True + True)
print(False + False)

print('and or not is and in Keywords in Python')
print(3 and 0 and 1)
print(1 and 6 and 0)
print(6 and 9 and 11)
print(5 or 1 or 2 or 3)
print(1 or 3 or 9 or 7)
print(0 or 0 or 0 or 9)

print(not True)
print(not False)
print(not 3)
print(not 0)

print('is keyword is used if two values are at same memory Location')
print('' is '')
print({} is {})
print([] is [])

print('in keyword in case sensitive')
x="Gurnani Hiren"
if "hiren" in x:
    print('Present')
else:
    print('Not present')

x="Gurnani Hiren"
if "Hiren" in x:
    print('Present')
else:
    print('Not present')


print('For while continue and break statement in Python.')
print('For statement')
for i in range(5):
    print(i,end=" ")

for i in range(0,5):
    print(i,end=" ")
print('\n')
print('While statement')
i=0
while i < 10:
    print(i,end="\n")
    i=i+1

print('Break statement in Python')
for i in range(10):
    if i == 6:
        break
    else:
        print(i,end="\n")

print('Continue statement in Python')
i=0
while(i<10):
    if i == 7:
        i=i+1
        continue
    else:
        print(i,end="\n")
        i=i+1


print('Def Keyword in Python')

def add():
    a=5
    b=5
    x=a+b
    print(f"Addition of two numbers is {x}")

add()
print('Passing Arguments in function')
def add(n1,n2):
    x=n1+n2
    print(f"Addition of two numbers is {x}")

add(10,15)
add(3.5,11)
add('Gurnani','Hiren')

print('Return keyword in Python')
def sub(n1,n2):
    x=n1-n2
   # return x

result=sub(10,5)
print(type(result))
print(f'subtraction of two numbers is {result}')

print('Function returning Multiple values through List')
def func1(x,y):
    n1=x
    n2=y
    return [n1,n2]

x=func1('hiren',790)
print(x)
print(type(x))

print('Function returning Multiple values through tuple')
def func2(x,y):
    return (x,y)

x=func2('hiren',790)
print(x)
print(type(x))

print('Function returning Multiple values through sets')
def func3():
    return {1,2,3}

x=func3()
print(x)
print(type(x))

print('Function returning Multiple values through dictionary')
def func4():
    x=dict()
    x["str"]="Gurnani"
    x[1]=10
    x["str2"]="Waheguru"
    return x

x=func4()
print(x)
print(type(x))



print('None Keyword in python')
print('None means nothing.none is not equal to Null or empty string list etc,None can be assigned to variables')
print(None == [])
print(None == '')
print(None == ())
x=None
print(x)
print(None == None)


print('Import and Math Keyword in Python')
import math
print(math.factorial(5))
from math import factorial
print(factorial(6))

print('Pass keyword in python')
print('Pass keyword is used to do nothing.')
for i in range(10):
    pass


print('Del keyword in Python')
string="Gurnani Hiren"
#del(str[0])
print(string)
del string
#print(string)

l=[1,2,3,4]
del(l[0])
print(l)
del(l)
#print(l)


print('as keyword in Python')
import math as hiren
print(hiren.factorial(2))

print('Yeild keyword in Python')

def func5():
    sum=0
    for i in range(20):
        sum=sum+i
        yield sum

x=func5()
for i in x:
    print(i,end=" ")


print('Another Function explaining yeild')
def func6():
    sum=0
    for i in range(20):
        if i % 2 == 0:
            yield i

x=func6()
for i in x:
    print(i,end="\n")



class company():

    company1="Hp"
    company2="samsung"
    company3="dell"

    def fun(self):
        print(f'1st company is{self.company1}')
        print(f'2nd company is{self.company2}')
        print(f'3rd company is{self.company3}')


x=company()         #Object Instantiation
print(x.company1)
print(x.company2)
print(x.company3)
x.fun()


print('Exception Handling Keyword')



                

