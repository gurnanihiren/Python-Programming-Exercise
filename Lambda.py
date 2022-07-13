

x="Gurnani Hiren"
print(lambda x:print(x))    #Lambda returns address of Object.
y=lambda x:print(x)
print(y("Gurnani Hiren"))

#We can direct pass Value in Lambda Function without calling it directly.
#Lambda Function can directly Invoked.
x="Gurnani Hiren"
(lambda x:print(x))(x)      #(lambda x:print(x))("Gurnani Hiren")
 
double=lambda x:x*2
print(double)

y=lambda z:z/2
print(y)

z=lambda x,y,h:x+y+h
print(z)


#Filter Method


def Func1(variable):
    x=[1,2,3,44,55,66,77,88,99]
    for i in x:
        for j in variable:
            if(i == j):
                yield j
            else:
                pass
variables=[1,2,3,4,5,6]
m=Func1(variables)

for i in m:
    print(i)


def hiren(x):
    print('Inside Func3')
    List=['e','h','e','g']
    print(x)
    print(List)
    for i in List:
        for j in x:
            if(j == i):
                yield j
            else:
                print('Not present')


sequence = ['a','i']
print(sequence)
filtered_items=filter(hiren,'a')
print(type(filtered_items))
print('Outside Function')
for i in filtered_items:
    print(i)



def add(x):
    print(x)
    for i in x:
        if i > 15:
            yield i 
        else:
            pass

m=[12,16]

ans=filter(add,m)
for i in ans:
    print(i)
