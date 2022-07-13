
print('\n')
print('Comments in Python')
print('# is used for single Line comment')
print('Multi Line Comments are done using triple-single Quotations \n')

#singlelineComemnt


'''
    Multi Line Comment'

'''
print('________Python Keywords_______')
import keyword
print(f'Total No of keywords in Python are {(keyword.kwlist)}')

count=0
for i in keyword.kwlist:
    count=count+1

print(f'Total No of Keywords in Python are{count} \n')

print('Quotations in Python \n')
print('String can be Created using single,double,triple-single quotes,Double-single quotes \n')
x='Hiren'
print(x,end="\n")
x="Hiren"
print(x,end="\n")
x='''Hiren'''
print(x,end="\n")
x="""Hiren"""
print(x,end="\n")
print("'gurnani Hiren'")
print("Hello 'World'!")
print('"Hello" World!')
print('It\'s Monday Today \n')


print('Multi Line Statements')
l=[1,2,3,
4,5,6,7]
print(l)


a=10
b=12
c=13
total=a + \
b + \
c
print(total)


x=(1,2,3,
4,5,6,
7,8)
print(x)

x={1,2,3,
4,5,
6,7}
print(x)

print('Python Lines and Indentation.')
x=10
if x > 10:
    print('x is greater than 10')
  #print('x')
elif x < 10:
    print('x is smaller than 10')
else:
    print('x is equal to 10')