
d={}
print(d)
print(type(d))
d=dict()
print(d)
print(type(d))
a=dict([(1,'Gurnani'),(2,'Waheguru')])
print(a)
b=dict({1:'Gurnani',2:'Waheguru'})
print(b)
c={1:'Gurnani',2:'Waheguru'}
print(c)

print(a == b == c)
print('Dictionary using Tuple as key')
d={(1,2,3):'Gurnani',(2,4,3):'Waheguru'}
print(d)

print('Dictionary using list')
#d={[1,2,3]:'Gurnani',[2,4,3]:'Waheguru'}
print('Dictionary using Sets')
#d={{1,2,3}:'Gurnani',{2,4,3}:'Waheguru'}

print('Dictionary using Assignment')
d={}
d[1]='Gurnani'
d[2]='Waheguru'
print(d)
d[3]='Hiren'
print(d)

d={1:'Gurnani',2:'Waheguru'}
x=str(d)
print(f'Dictionary Converted to string is {x}{type(x)}')
print('Dictionary Methods in Python')
d={1:'Gurnani',2:'Waheguru'}
print(f'Original Dictionary is {d}')
d.clear()
print(f'After removing dictionary is {d}')


h={1:'Gurnani','Waheguru':2,'Himanshu':3}
print(list(h)) #Returns List of keys
h={1:'Gurnani','Waheguru':2,3:""}
print(len(h))

x={'Gurnani':'Hiren',1:'Waheguru'}
print(f'Type of x is {type(x)}')

d={1:'Gurnani',2:'Waheguru',3:[1,2,3]}
print(f'Original Dictionary is {d}')
import copy
x=copy.copy(d)  #Returns Shallow Copy of dictionary.
print(f'After copying value of x becomes{x}')
x[1]='Waheguru'
x[2]='Gurnani'
x[3]=[2,3,4]
print(f'After making changes of x becomes {x}')
print(f'Original dictionary is {d}')

import copy
d={1:'Gurnani',2:'Hiren',3:'Waheguru',4:{'A':(1,2,3,4),'B':(3,4,5)}}
print(f'Original Dictionary is {d}')
x=copy.deepcopy(d)
print(f'Copied dictionary is {d}')
x[1]='Waheguru'
x[2]='Hiren'
x[3]='Gurnani'
x[4]['B']=(11,12,13)
print(f'After changing Original dictionary is {x}')
print(f'Origianl dictionary is {d}')

print('dict from keys Functions')
d={}
seq={1,2,3,4}
print(d.fromkeys(seq))
seq=(1,2,3,4)   #[1,2,3,4]
print(d.fromkeys(seq))
x={'sls':1,'Waheguru':2}
print(d.fromkeys({'Gurnani','Hiren'},x))    #List and sets create Nested
print(d.fromkeys(x,"Gurnani"))              #key values are updated.
seq=(-1,-2,-3)
print(f'with list and value is {d.fromkeys(["Gurnani"],seq)}')
print(f'sequence is {d.fromkeys(seq,11)}')
x={1:'Gurnani',2:'Waheguru',3:'Indiana'}
print(d.fromkeys(x,'sls'))
print(f'Original Dictionary is {d}')

print('get Method in Dictionary')   #get Method-key,value #Original remains same
print('________________________')
d={'1':'Gurnani',2:'Waheguru'}
print(d.get(3))
print(d.get(-1))
print(d.get('1'))
d.get('1')
print(d)
print(d.get('Waheguru',12))

print('has-key in Python')
print('_________________')
d={1:'Gurnani',2:'Waheguru'}
#print(d.haskeys('1'))  #Reurns True if value Found else false.
#print(d.haskeys('2'))
if 1 in d:
    print('True')
if 'Gurnani' in d:
    print('True')
else:
    print('False')

print('Items Method in Dictionary')
print('__________________________')
x={1:'Gurnani',2:'Waheguru',3:'Indiana'}
print(x.items())
x={'Indiana':'Nevada',2:3}
print(type(x.items()))

print('keys Method in Dictionary')
print('_________________________')
x={1:'one',2:'Two',3:'Three',4:'Four'}
for i in x:
    print(f'key in dictionary is {i},{x[i]}')

x={'one':1,'Two':2,'Three':3,4:5}
for i in x:
    print(f'key in dictionary is {i},{x[i]}')

x={'one':1,'Two':2,'Three':3,'Four':4}
print(x.keys())
x={'Waheguru':'One','Two':2,'Hiren':'Waheguru'}
print(x.keys())

x='one'
d={'one':1,'Two':2,'Three':3,'Four':4}
if x in d.keys():
    print('x is present in d')
else:
    print('x is not present in d')

print('set-default Method in Dictionay')
print('_______________________________')
#set-default-(key,value)Pair returns value of key
#if key not present adds key with None value.
#Case sensitive
x={'one':1,'Two':2,'Three':3}
print(f'value of key "one" is {x.setdefault("one")}')
print(f'value of key "two is {x.setdefault("two")}')
x.setdefault('Four',4)
print(f'Original Dictionary is {x}')
x.setdefault('Five')
print(f'Value of Dictionary is {x}')
print(f'If key not present returns  {x.setdefault("six")}')

print('dict.values in Python')
print('_____________________')
x={1:'One',2:'Two',3:'Three',4:'Four'}
print(f'values in Dictionary is {x.values()}')
x={'Gurnani':2000,'Vikram':3000}
print(f'values in Dictionary is {x.values()}')
print(type(list(x.values())))

x={'one':1,'Two':2,'Three':3,'Four':4}

for i in x.values():
    print(f'values are {i}')

print('update Method in Dictionary')
#Does not returns anything.
x={'one':1,'Two':2,'Three':3,'Four':4}
x.update([('one','Waheguru')])
print(f'Updated Dictionary is {x}')
d={'Five',5}
x.update([d])
print(f'updated dictionary is {x}')


print('Dict Compression in Python')
L=[2,3,4]
#y=[x:x*2 for i in L]
#print(f'Dictionary using Dict Compression is {y}')

print('String uppercase and Lowercase without Inbuilt Function')
def calculate(string):
    lowercase,uppercase,special_character=0,0,0
    digits=0
    for i in string:
        print(i,end="")
        if i>='A' and i<='Z':
            uppercase=uppercase+1
        elif i>='a' and i<='z':
            lowercase=lowercase+1
        elif i>='0' and i<='9':
            digits=digits+1
        else:
            special_character=special_character+1

    print(f'Uppercase in string is {uppercase}')
    print(f'Lowercase in string is {lowercase}')
    print(f'special_character in string are {special_character}')
    print(f'Digits in string are {digits}')
x=input('Enter a string:')
calculate(x)
 
print('Fibonacci Series in Python')
#0 1 1 2 3 5 8 13

L=[]
a,b=0,1
L.append(a)
L.append(b)
for i in range(15):
    c=a+b   
    L.append(c)
    a=b
    b=c 

print(f'Fibonacci Series is {L}') 

#Reverse a Number 12323
x=int(input('Enter a Number:'))
y,rem=0,0
while x > 0:
    rem=x%10 
    y=y*10+rem  
    x=x//10     
print(f'Reverse of a Number is {y}')

#"Gurnani"
#Reverse a string
x=input('Enter a string:')
print(f'Original string is {x}')
length=len(x)
i=0
string=""
while length>i:
    string=string+x[length-1]
    length=length-1   

print(f'Reverse of a string is {string}') 

print('Concatenation of two strings without Join Method')
L=['u','g']
string="Gurnani"
z=""
for i in L:
    z=z+string+i
print(f'Concatenation of strings is:{z}')

x=[]
y=[1,2,3,4]
z=x+y
print(f'Concatenation of list is {z}')
print('Concatenation in List without Append Mode.')
L=[]
L=L+['Gurnani']
print(f'Concatenated List is {L}')
L+=[1,2]
print(f'Concatenated List is {L}')
L+='G'
L+='u'
L+='R'
print(f'Concatenated List is {L}')

print('Count Method in List Manually')
L=[1,1,2,3,4,5,"Gurnani",2,3,"Waheguru","Gurnani",11,1,12]
count=0
for i in L:
    if i == 1:
        count=count+1
    else:
        pass
print(f'Number of 1\'s in List is {count}')
i=1
print(type(i))
'''
print('Remove Method in List Manually')
L=[1,2,3,"Gurnani"]
j=0
x=int(input('Enter a variable to remove From List:'))
#length=len(L)
for i in L:
    if i == x:
        j=i
        for j in L:
            L[j]=L[j+1]
        L=L-1
print(f'After Removing list becomes {L}')
    '''




    




