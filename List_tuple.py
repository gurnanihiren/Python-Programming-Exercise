print('Built in List Functions')

L=[1,2,3,4,5]
print(max(L))
print(min(L))
L=["Gurnani","Hiren","Nevada","Indiana","Boston"]
print(min(L))
print(max(L))
L=[[1,2,3],[4,5,6,7],[8,9,10,11]]
print(max(L))
print(min(L))
x=list()
print(x)
x=list('Geeks')
print(x)

print('Built in methods in List')
print('Append Method in List')#Dosent Returns anything
L=[]
L.append('Geeks')
print(L)
L.append('g')
print(L)
L.append([1,2,3])
print(L)
L.append(1)
print(L)
L.append(3.3)
print(L)
L.append((1,2))
L.append({1,2,3})
L.append({'Gurnani':'Hiren','sLs':'Company'})
print(L)
L.append(None)
print(L)

print('Count method in Python')
L=[1,21,"Hiren",2,1,1,2,3,4,"Hiren",[1,2],[1,2]]
#print(list.count[1])
print(L.count(1))
print(L.count("Geeks"))
print(L.count(None))
print(L.count(3.3))
print(L.count([1,2]))
#print(L.count(1,2))

print('Extend Method in List')#Returns nothing But Modifies Original list
#Add multiple elements but over iterable
L=[]
L.extend('Geeks')
L.extend(['geeks'])
L.extend([1,2,3])
L.extend([[1,2,3,4,5]])
print(L)
L.extend({1,2})
L.extend({1:'Gurnani',2:'Hiren'})   
print(L)
#L.extend(None)

print('Index Method in List')   #Returns Index in python
L=[1,23,3,5,"Gurnani","Hiren",1.1,1]
print(L.index(1))
#print(L.index(1,3,6))  -Value Error.
print(L.index("Gurnani"))
print(L.index(5,-6,-1))
print(L.index(5,2)) #Will count from 2
print(L.index(23,0))
print(L.index("Gurnani",-6))
#print(L.index(23,7,2)) ValueError notpresent
#print(L.index(3,-1,-7))#ValueError notpresent

print('List Insert Method in List') #insert(index,element)
L=[1,2,3,"Gurnani","Waheguru"]
L.insert(7,"Hiren")
L.insert(100,"sls")
L.insert(-8,"Anand")
L.insert(-100,"Nadiad")
print(f'After inserting List becomes {L}')

print('Pop method in List') #pop(Index)-By default last element.
L=[1,23,3,5,"Gurnani","Hiren",1.1,1]
print(f'Before poping List becomes{L}')
print(L.pop())  #Modifies Original List
print(L.pop(3))
print(L.pop(-5))
print(f'After poping List becomes{L}')
#If Index Out of range throws Error

print('Remove method in List')


print('Reverse method in List')
L=['Gurnani','Waheguru',3,4]
print(f'Original List is {L}')
L.reverse()   #Returns None and Modifies original List.
print(f'After Reversing List becomes {L}')
L=[1,2,3,4]
print(f'Original List is {L}')
L.reverse()
print(f'After Reversing List becomes {L}')
L=[1,2,{1:'Hiren',2:'Waheguru'},{1,23},(11,21)]
L.reverse()
print(L)

print('Remove Method in Python')    #Returns None
L=[1,2,3,4,"Gurnani","Renu","Waheguru",1,2,3]
L.remove("Gurnani")
#L.remove("Hiren")
L.remove(1)
L.remove(2)
print(f'After Removing List becomes {L}')

print('sort Function in Python')
L=[1,2,3]
L.sort(reverse = True)  #In descending Order.Highest upper
print(L)
L=[33,22,11,545]
L.sort(reverse = True)
L=["Gurnani","Indiana","Nevada","Hiren"]
L.sort()
print(L)
L.sort(reverse = True)
print(L)

print('Built in Tuple Functions')
x=tuple()
print(x)
x=tuple('Geeks')
print(x)
x=(1,2,"gurnani","sls")
print(f'length of tuple is {len(x)}')
x=(1,2,3,101,13)
print(f'Maximum of Tuple is {max(x)}')
print(f'Minimum of Tuple is {min(x)}')

print('Dictionary Built in Functions')
x=dict()
x[1]="sls"
x[2]="Gurnani"
x[3]="Waheguru"
#x['ABC']=10
print(f'Len of dictionary is {len(x)}')
print(f'Max in Dictionary is {max(x)}')
print(f'Min in Dictionary is {min(x)}')
#y=dict([[1,[['Gurnani','Hiren'],['Waheguru','Gurunanak']]],[2,'Waheguru']])
y=dict()
y[1]={}
y[1]['Abc']='def'
y[1]['Gurnani']='Hiren'
y[2]=3
#y['xyz']={}
#y['xyz'][1]='Anand'
#y['xyz'][2]='Nadiad'
print(max(y))
print(min(y))
print(y)

d=dict()
d['1']='Gurnani'
d['2']='Hiren'
print(str(d))
y=str(d)
print(type(y))

d=dict()
print(type(d))

print('Dictionary Methods in Python')
