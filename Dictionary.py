
print('Dictionary is key:value pair')
x={1:'Geeks',2:'For',3:'Geeks'}
print(x)

print('Empty Dictionary')
x=dict()
print(x)

x=dict(Gurnani=1,Hiren=2,y=3,z=4)
print(x)

x=dict({1:'Gurnani',2:'Hiren',3:'Waheguru'})
print(x)

x=dict({(1,2),(3,4),(5,6)})
print(x)

x=dict([(1,'Gurnani'),(2,'Indiana'),(3,'waheguru'),(4,'Dell')])
print(x)


print('Mixed data Type Dictionary in python')
y={1:1,2:[1,2,3,4],3:'Gurnani Hiren',4:'Waheguru',1:'sls',1:'Indiana'}  #if Multiple Keys used it will used latest one with updated value but it
#will have one key only not duplicated ones. 
print(y)

print('Nested Dictionary')
x={1:'Gurnani',2:'Hiren',3:{'A':'sls','B':'waheguru'}}
print(x)

x={}
x[0]='Hiren'
x[1]='Gurnani'
x[2]='Waheguru'
print(x)

x['value_set']=[1,2,3,4,5]
print(x)

x[3]={'Anand':{'vidyanagar':'Gujarat'}}
print(x)

print('Accessing Dictionary items')
x={1:'Gurnani',2:'Hiren',3:'SLS',4:{'state':'Gujarat','city':'Anand','Area':'Anand-Gidc'}}
print(x[1]) #Dictionary items can be accessed by key values
print(x[2])
print(x[3])
print(x[4]['state'])
print(x[4]['city'])
print(x[4]['Area'])

print('Accessing elements of Dictionary via Get Method')
print(x.get(3))
print(x.get(4))
#print(x.get(5,"Gurnani"))  #if key not present we can return default values.
#print(x.get(5))    -if key not present return None
#print(x.get('Hiren'))

print('Dictionary Methods')
print('clear in Dictionary')
x.clear()
print(x)

print('copy in Dictionary')
x={1:'Gurnani',2:'Waheguru',3:'Indiana',4:{'Gujarat':'Anand','Area':'gidc'}}
import copy
z=copy.deepcopy(x)
print(z)
z[1]='Hiren'
z[2]='Gurunanak'
z[3]='USA'
z[4]['Gujarat']='Nadiad'
print(f'Original Dictionary {z}')
print(f'Deep copied Dictionary is {x}')

y=copy.copy(x)
y[1]='Hiren'
y[2]='GuruNanak'
y[3]='USA'
y[4]['Gujarat']='Nadiad'
print(f'Original Dictionary is {y}')
print(f'Shallow copied Dictionary is {x}')

x={1:'Gurnani',2:'Waheguru',3:'Indiana'}
print(x)
y=x.items()        # print(x.items())
print(y)
del x[2]
y=x.items()
print(y)

print('Dictionary keys')    #Returns a List of Dictionary Keys
x={1:'Gurnani',2:'Hiren',3:'Waheguru'}
print(x.keys())
x=dict()
print(x.keys())
x.update({4:'SLS'})
print(x)

print('Update Method in Dictionary')
x={1:'Gurnani',2:'Hiren'}
y={3:'Waheguru'}
x.update(y)
print(f'Updated dictionary is {x}')

x={'Gurnani':1,'Hiren':2,'Waheguru':3}
y=x.values()
print(y)
print(sum(y))

print('Pop Function with Dictionary')
x={'Gurnani':1,'Waheguru':2,'sls':3}
print(x.pop('Hiren',7))     #pop-(key,default value)
print(f'Dictionary before deletion is {x}')
print(x.pop('Gurnani'))
print(f'New-Updated Dictionary is {x}')
#if key not present default value returned
#if key not present default value not provided ,returns error.

    
print('Pop Item in Python')
x={1:'Gurnani',2:'Waheguru',3:'Indiana'}
y=x.popitem()
print(y)