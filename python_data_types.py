
L=[1,2,3,4,5]
print(*L)
print('Assigning Values to variables to python')
print('________________________________________')
x=5
print(f"Value of x is {x}")
print(type(x))
y=3.3
print(f"value of y is {y}")
print(type(y))
z="sls"
print(z)
print(type(z))

print('Taking Input From user')
print('______________________')
x=int(input('Enter a value for x:'))
print(f"Value of x is {x}")
print(type(x))

y=input('Enter a value for y:')             #Only Input also returns str type.
print(f'value of y is {y}')
print(type(y))

z=float(input('Enter a value for z:'))
print(f'value of z is {z}')
print(type(z))


print('Multiple Assignment in Python')
print('______________________________')
x,y,z=input('Enter the value of x,y and z').split()     #input.split returns type of str
print('x y and z are',x,y,z)                              #int(input().split)   will never work lly with Float.
 
print('Taking Multiple values using List Compression')
print('_____________________________________________')
x,y,z=[int(w) for w in input('Enter three values').split()]     #of oint type.
print('value of x,y and z is',x,y,z)

x,y,z=[w for w in input('Enter three values').split()]              #of str type.
print(type(x))
print('value of x,y and z is',x,y,z)

print('Python Data Types')
print('_________________')
print('Numeric data Types are int of class int,Float of class float and Complex datatypes of class complex')
x=5
print(type(x))
x=3.5
print(type(x))
x=2+5j
print(type(x))

print('String data types are used to store chars of bytes')
print('__________________________________________________')
x='Hiren'
print(x)
x="Hiren"
print(x)
x='''Hiren'''
print(x)
x='''Gurnani    
     Hiren
     Anilbhai'''
print(x)


print('Accessing string Elements')
x="Gurnani"
print(x[0])
print(x[-1])


print('List Data Type--Ordered Collection-mutable=[]')
print('______________')
L=[1,2,3,4,5,"Gurnani",3.3,5.5,3]
print(f'List is {L}')
print('Accessing List Elements')
print(L[0])
print(L[1])
print(L[4])
print(L[-1])

print('Tuple Data Type--Ordered Collection-immutable=()')
print('_______________')
x=(1,2,3,4,5)
print(f'Tuple is {x}')
print('Accessing Tuple Elements')
print(x[0])
print(x[-1])
x=tuple('Geeks')    #Only accepts one arguments
print(x)

print('Boolean data Types in Python used to represent Boolean values')
print('_____________________________________________________________')
print(True == 1) 
print(False == 0)
print(True == 2)
print(True + True)
print(False + False)

print('Set data Type in Pythob--Unordered Collection,Mutable with no duplicate elements')
s=set('1')  #only accepts one agrument
print(s)
s=set('Geeks')
print(s)
s=set('3.3')
print(s)
s=set(('Gurnani',2,3,4,5))  #Set with Tuple
print(s)
s=set([1,2,3,'Gurnani',5,6,7])  #set with List
print(s)

print('Accessing element from sets:')
i=0
for i in s:
    print(i,end=" ")

print('Dictionary Data Type in Python--unordered Collection in key-value pair,keys are case sensitive,must be unique')
print('______________________________')

#z=dict([(1,"Gurnani"),(2,"Hiren")])                     #Dictionary using List
z=dict(((1,"Gurnani"),(2,"Hiren")))
y={1:"Gurnani-Hiren",2:"Waheguru ji"}                   #Dictionary using sets
x=dict({1:'Hiren',2:'Waheguruji'})                      #Dictionary using dict Function

print(x)

print('Accessing elements of Dictionary')
print(y[1])
print(y[2])
print(z)
#print(y[3])        --If not present it will return Key Error.

print(z.get(1))             
print(z.get(2))
#print(z.get(3))    --If key not present it Will return None.

print('Type Conversion in Python.')
print('__________________________')
s="10101"
x=int(s,2)  #Converts string to int
print(x)
x=float(s)  #convert string to float
print(x)


s='A'
x=ord(s)    #used to convert character to int 
print(x)
s='4'       #used to convert character to int
x=ord(s)
print(x)
s=56
x=hex(s)    #used to convert Integer to hexadecimal string
print(x)
s=56
x=oct(s)    #used to convert Integer to octal string.
print(x)


s="Gurnani"
x=tuple(s)          #string to tuple
print(x)
x=list(s)           #string to List
print(x)
x=set(s)            #string to set
print(x)

s=((1,"Gurnani"),(2,"Waheguru"))    #Tuple to Dictionary.
x=dict(s)
print(x)
s=[(1,"Gurnani"),(2,"waheguru")]    #List to Dictionary.
x=dict(s)
print(x)

a=1
b=2
c=complex(a,b)      #Converting Integers to complex Numbers.
print(c)
c=str(a)            #Converting integers to string.
print(c)


#Convert Integers to Ascii Values.
x=56
c=chr(x)
print(c)

x=65
c=chr(x)
print(c)