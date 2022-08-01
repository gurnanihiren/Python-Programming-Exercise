
#print Multiplication Table of a Number

n=int(input('Enter a Number to generate its Multiplication Table:'))
mul=1
for i in range(11):
    mul=n*i
    print(f'{n}*{i}={mul}')