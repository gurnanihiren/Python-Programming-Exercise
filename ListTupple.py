
#13/07/2022
#Wednesdasy.

#Example showing empty List.
L=[]
print()

L=[1,2,3,4]     #List containing Integers.
print(L)

L=["Gurnani Hiren","Hiren","Waheguru"]  #List containing strings.
print(L)

L=[2.2,3.3,4.4,5.5]        #List containing Floats.
print(L)        

L=[1,2,3,"Gurnani","sls","waheguru",3.3,4.5,6.7]    #List containing strings,floats,integers.
print(L)

L=[(1,2),{1,2,3,4,5},{1:"Gurnani",2:"Hiren"}]   #List containing Tupple,Dictionary,Sets.
print(L)

L=[1,1,1,2,2,3,3,4,4,5,3,1,"sls","Gurnani","sls"]    #List containing Duplicate elements.
print(L)

L=[]
print(len(L))

L=[1,2,3,"Gurnani",4,5]
print(len(L))

#Empty List using list() Function.
L=list()        #list()Function creates List.         
print(L)
print(len(L))

#MultiDimensional List
List=[[1,2,3],["Gurnani","Hiren","Waheguru"]]
print(List[0])
print(List[1])
print(List[0][0])
print(List[0][1])
print(List[0][2])
print(List[1][0])
print(List[1][1])
print(List[1][2])
print(f"Length of 2d List is {len(List)}")
L=[ [ [1,2],[3,4]] , [[5,6],[7,8] ] ]
print(L[0][1][1])

#Inbuilt List Methods
#append Function is used to add one item in Last in Python.
print('Append Method in List')
L=[]
L.append(1)
L.append(2)
L.append("Gurnani")
L.append("Sls")
print(L)
L.append(0)
print(L)
L.append(3.4)
L.append(4.5)
print(L)
x=(1,2,3)       #Appending Tuple
L.append(x)
y={1.1,2.2}     #Appending Sets
L.append(y)
z={1:"Gurnani",2:"Waheguru"}    #Appending Dictionary
L.append(z)
print(L)

#Copy in string Functions
#Returns original copy of List without Modifying original List.
print('Copy Method in List')
L=[1,2,3,4,[1,2]]
x=L.copy()
print(x)

#insert Method in List
print('Insert Method in List')
L=[1,2,3,4]
L.insert(10,(1,2,3))
print(L)
L.insert(-90,{1:"Geeks",2:"Waheguru"})
print(L)
L.insert(-1,"Geeks")    
print(L)
L.insert(-2,"Gurnani")
print(L)
L.insert(0,"Waheguru")
print(L)

#Extend in List--------#Does not add tupple sets and dictionary converts them and extends the List.
print('Extend method in List')
L=[]
L.extend([1,2,3])
L.extend('Hiren')
L.extend(("Waheguru",1,2.3))
L.extend({5,6,7})
print(L)


#Accessing elements of a List.
print('Accessing elements of a List')
L=[1,2,3,"Hiren","Gurnani"]
print(L[0])
print(L[1])
print(L[-1])
print(L[-2])
#print(x[54])--List Index Out of Range

#Reverse a List and replaces Original List with Reversed List
print('Reversing a list')
print(L.reverse())      
print(L)    #List is Modified.

#Remove Element From List. #Remove desired element.
print('Remove Method in Pyhton')
L=[1,2,3,4,5]
L.remove(4)
print(L)
L=["Hiren","Gurnani",1,2,3,4,"Hiren"]
L.remove('Hiren')
print(L)
L=["Gurnani",1,2,"Waheguru"]
#L.remove("Renu")                        #Throws Error   #x not in List


#Pop Method in List.
print('Pop method in Python')
L=[1,2,3,4,5]
L.pop()
print(L)
#L.pop(100)--------------#Index Error Index Out of range pop(index)

#L.pop(-20)--------------#Index Error Out of range

L.pop(2)
print(L)

print('Slicing in Lists in Python')
L=[1,2,3,4,"Gurnani","Hiren","SLS","Mona","sona","kona","harsh"]
print(L[0:])
print(L[4:])
print(L[:])     #To Print all elements in List.
print(L[2:6])
print(L[4:10])
print(L[:-1])
print(L[-7:-2])
print(L[-50:])
print(L[:-4])
print(L[::-1])
print(L[-2:-7]) #Will print Nothing just empty List,so Reverse Indexing is not possible,possible just to print List without error.
print(L[8:3])   #Will print Nothing just empty List.

print('Sorting in List')
print('In Ascending Order')
L=[4,6,7,3,2,1,8,7,9]
L.sort()
print(L)
print('In Descending Order')
L.sort(reverse=True)
print(L)

L=[4.4,3.3,1.1,7.7,6.7,5.5]
print('In Aescending Order')
L.sort()
print(L)
print('In Desending Order')
L.sort(reverse = True)
print(L)

L=["Geeks","Hiren","Waheguru","krishna","Mahadev"]  #Compares ascii
print('In Ascending Order')
L.sort()
print(L)
print('In Descending Order')
L.sort(reverse = True)
print(L)

#L=["Geeks","Nadiad","SLS",1,2,3,4.4,5.5]--Mixed Type sort does not works.
#L.sort()

print('Count Method in List')   #Case sensitive #If more than 1 paramaeter send in count will result in Type error.
L=[1,1,1,2,3,4,5,4,5,6]
print(L.count(1))
L=["Geeks",1,2,"Geeks","Hiren","SLS"]
print(L.count("geeks"))
print(L.count("SLS"))

print('Clear method in List')   #Deletes All elements in List in Current List and returns empty list
L=["Geeks",1,2,3,4,"Waheguru",3.3]
L.clear()
print(L)

print('Index Method in List in Python' )        #INDEX(ELEMENT,start and stop index for searching optional.)--if index 0 to 4 then will go till n-1 indexes.0,1,2,3.

L=[1,2,3,"Utah","New-Orleans","Arizona","nevada","New-Orleans","utah",1,2,3]
print(L.index(1))
print(L.index("Arizona"))
print(L.index("nevada",2,8))
print(L.index("nevada",3))
#print(L.index("utah",0,3))
#print(L.index(3.3))--If value Not present in List-Throws Error.
#print(L.index("Utah",5,15))-Throws Error.


#Buildin List Functions
print('len-Function')
x=[1,2,3,4,5]
print(f"Length of Given string is:{len(x)}")
print('Max and Min Function in List')
x=[55,44,33,2,1,5,6]
print(f"Max in Given List is {max(x)}")
print(f"Min in Given List is {min(x)}")
print('List Function in Python')
x=[1,2,3,4,5]
y=list(x)
print(y)


print('All Functions and Methods in One List')
print('_____________________________________')
L=[1,2,3,4,5,"Arizona","Sls","Nevada","Arizona"]
L.append(5)
print(L)
print(L.count("Arizona"))
print(f"Length of List is {len(L)}")
#print(f"Maximum of List is {max(L)}")
#print(f"Minimum of List is {min(L)}")
x=L.copy()
print(f"Copied List is {x}")
print(f'Index of Arizona is {L.index("Arizona")}')
print(f'Count of Arizona is {L.count("Arizona")}')
#print(f'Sorting in Ascending Order is {L.sort()}')
#print(f'Sorting in Descending Order is {L.sort(reverse = True)})
L.pop()
print(f'After Popping List becomes {L}')
L.remove("Arizona")
print(f'After removing List becomes {L}')   #Removes First Matched string or Number
L.extend([11,12,13])
print(f'After extending List becomes {L}')
L.insert(14,5)
print(f'After Inserting value 14 List becomes {L}') 
L.reverse()
print(f'After Reversing Value List becomes {L}')
L.clear()
print(f'After clearing the List,List L becomes {L}')


print('Tuple in Python')
print('_______________')
x=(1,2,3,4,5)
print(x)
x=(2,3,4,5,"Geeks","Hiren","Waheguru")
print(x)
L=[1,2,3,4,5]
x=tuple(L)
print(x)
print('Concatenation of Tuple')
x=("Arizona","Nevada","Utah")
y=(1,2,3)
print(x + y)    #Concatenation 

#Indexing and Slicing in Tuple
x=(1,2,3,4,"Hiren","Indiana","Arizona","Waheguru")
print(x[0])
#print(x[9])--Tuple Index Out of Range
#print(x[-9])--Tuple Index Out of Range

#Slicing in Tuple
print(x[::-1]) #Reversing Tuple
print(x[:])    #Print All elements
print(x[1:3])
print(x[:5])
print(x[2:])
print(x[:-4])
print(x[-7:-2])

#Tuple-Built in Functions
x=(1,2,3,4,"Hiren","sls","Hiren","Waheguru","Indiana",1,2,3)
print(x.index(3,1))
print(x.index("Hiren"))
#print(x.index(3,3,10))----will check between 3 to 9
print(x.count("Hiren"))
print(x.count(1))


#Built in Methods in Tuple
x=tuple()
print(f"Empty Tuple is {x}")
x=(1,2,3,4,5,6)
print(f"Tuple is {x}")
z=tuple(x)
print(f"Sequence using tuple Method is {z}")
m=(22,33,4,44,11,99)
print(f'Max From Tuple is {max(m)}')
print(f'Min From Tuple is {min(m)}')


'''
#Taking Input in Python FOR List using for loop
L=[]
print('Taking Input From user') #Taking int input in Python.
n=int(input('Enter a value for no of inputs in List:'))
for i in range(n):
    x=int(input(f'Enter a value for {i}:'))
    L.append(x) 

print(f"List items are:{L}")

L=[]
print('Taking Input from user')
n=int(input('Enter a value for no of inputs in List'))
for i in range(n):
    x=input(f'Enter a value for {i}:')
    L.append(x)

print(f"List items are:{L}")

'''




