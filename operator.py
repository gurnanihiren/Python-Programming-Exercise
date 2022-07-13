 

print('Operators in Python') 

print('___________________') 

print('Arithmetic Operators') 

  

x=int(input('Enter the values of x')) 
y=int(input('Enter the value of y')) 
print(f"Value of x is {x}") 
print(f"Value of y is {y}")
z=x+y 
print(f"Addition of two Numbers is {z}") 
z=x-y 
print(f"Subtraction of two Numbers is {z}") 
z=x*y 
print(f"Multiplication of two Number is {z}") 
z=x/y 
print(f"Division of two Number is {z}") 
z=x**y 
print(f"Exponent power of x to the y is {z}") 
z=x//y          #Floor division is also called Integer division it truncates decimal part.
print(f"Floor of x to the y is {z}") 

  

print('Comparision/Relational Operator') 

print('Comparision Operator return True or False based upon Comparision') 

print('_____________________') 

x=int(input('Enter the value of x')) 
y=int(input('Enter the value of y'))
print(f"Value of x is {x}") 
print(f"Value of y is {y}") 

print(x > y) 
print(x < y) 
print(x == y) 
print(x != y) 
print(x >= y) 
print(x <= y) 

  

print('logical Operators in Python') 
print('____________________________') 
print(3 and 10 and 0) 
print(0 and 10 and 15) 
print(1 or 5 or 0) 
print(0 or 0 or 5 or 6 or 7) 
print(not True) 
print(not False) 
print(not 5) 
print(not 0) 

  

print('Identity Operator in Python') 
print('____________________________') 
x=''    
b="Gurnani Hiren" 
c=''    
print(x is not b) 
print(x is c)               #is is used to check Memory address of two Variables.
a=' ' 
b=[] 
print(a is not b) 
print(a is b) 

  

print('Membership Operator in List') 

print('____________________________') 

x=int(input('Enter the value of x:')) 

a=[11,12,13,14,15,16,17] 

if x in a:                  #in Operator checks if value is present in a
    print('True') 
else: 
    print('False') 

     
if x not in a:              #not in Operator checks if value is not present in a
    print('True') 
else: 
    print('False') 


print('Bitwise Operator in Python') 

print('_____________________________') 

x=int(input('Enter the value of x:')) 
y=int(input('Enter the value of y:')) 
print(f"Bitwise And Operation is :{x&y}") 
print(f"Bitwise Or Operation is :{x|y}") 
print(f"Bitwise not Operator is:{~x}") 
print(f"Bitwiaw not Operator is :{~y}") 
print(f"Bitwise X-or operation is :{x^y}") 
print(f"Bitwise Right shift Operator on x:{x>>2}") 
print(f"Bitwise Left shift Operator on x:{x<<2}") 
print(f"Bitwise Right shift Operator on y:{y>>2}") 
print(f"Bitwise Left shift Operator on y:{y<<2}") 

print('Chaining of Operatos')
