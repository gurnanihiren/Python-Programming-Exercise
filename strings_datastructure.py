
s='Hello,World!'
print(s)
s="Hello World!"
print(s)
s='''Hello World!'''
print(s)

#s='It's Friday Today'                                      
s='It\'s Friday Today'
print(s)


s=76        #int value
x=str(s)
print(s)
print(type(s))

print('Taking input From user For string')
s=input('Enter a string:')                                 
print(s)                                                    
print(type(s))

print('Operations on string')

x="Hello" + "World"                                         
print(x)

print("Gurnani" > "hiren")                                   

s="Sls"
print(s*(3))                                                 

print("" != "Gurnani")                      #"" is treated as False." " is treated as True.
print("Hiren" == "Hiren")

print('Logical Operation on strings')

print(" " and "hiren")                                       
print("Gurnani" and "Waheguru")
print("" or "Gurnani")                                          
print('Waheguru' or 'Gurnani')
print(not "")
print(not "Hiren")


print('String Deletion with Del Keyword')

string="Gurnani"
#string[0]='H'                                                     
string="Hiren"                                                     
#del(string[0])                                                              
#del(string)                                                                
#print(string)

print('Iteration Over Strings using For Loop in Python')

string=input('Enter a string:')
for i in string:
    print(i,end="")
print()
string=input('Enter a string:')
length=len(string)                                                               #13--0 to 12
print(f"Length of a string is {length}")
print('Iterating string using While Loop')

i=0
while(i < len(string)):
    print(string[i],end="")
    i=i+1


print('in Operator in String')
x="sls"
if 'l' in x:
    print('Present')
else:
    print('Not Present')

print('Indexing in string')
x=input('Enter a string:')
print(x[0])                                     #If empty string,Index Out of range error
#print(x[4])                                     

print('String Slicing in Python')
x=input('Enter a string from user')
#Reverse Indexing not possible in slicing.
print(x[0:])
print(x[6:])
print(x[2:6])
print(x[-6:-3])
print(x[-8:-2])
print(x[111:200])       #It will Not throww error Like indexing if index is Out of range.
print(x[-95:-2])
print(x[6:2])           #Reversing range will Not throw an error but it will print Nothing.
print(x[-2:-6])         #Reversing range will Not throw an error but it will print Nothing.

print("Reversing String in Python")
print(x[::-1])
#print(x[::-100])       #Will Not throw an error.#Undefined Behaviour.


print("Formatting of string")
print("____________________")
print("sls is a {} based Company".format("Product"))
print("Value of x,y and z is {} {} {}".format(1,2,3))
print("My name is {}{}".format("Gurnani","Hiren"))
print("This is {},{} and {}".format("one","two","three"))
print("{2}{0}{1}{2}".format("GuruNanak","Guru-Angad","GuruAmardas","GuruRamdas"))                    #if Index Out of range it will throw an error.
print('{g}{h}{g} has nice tutorial for Python programming'.format(g="geeks",h="for"))



print("Sting Built in Functions.")

x=input('Enter a string:')
print(x.capitalize())
print(x.upper())
print(x.lower())
print(x.count("Waheguru"))
print(x.find("Wahe"))
#print(x.index("he"))

#split Method in Python.
y="Gurnani#Hiren#Waheguru"
print(y.split('#'))
y="GurnanitHirentWaheguru"
print(y.split('t'))
y="Gurnani Hiren Anilbhai"
print(y.split( ))
y="Gurnani$Hiren$Anilbhai"
print(y.split('$',-5))
y="Gurnani%Hiren%Anilbhai"
print(y.split('%'))

#splitness Method in Python.
y="Gurnani\rHiren\rAnilbhai\rWaheguru\rGurunanak"
print(y.splitlines())
print(y.splitlines(True))
y="Gurnani\nHiren\nAnilbhai\nWaheguru\nGurunanak"
print(y.splitlines())
y="Gurnani\vHiren\vAnilbhai\vWaheguru\vGurunanak"
print(y.splitlines(4))

#replace Method in Python.
x="geeks for geeks geeks for geeks for geeks"
print(x.replace("geeks","GEEKS",2))
print(x.replace("e","ea",5))
print(x.replace("ee","aa",3))
print(x.replace("geeks","geeksFORGeeks",2))
print(x.replace("geeks","geeksForGeeks"))
print(x.replace("the","geeks"))

#Strip Method in Python
x="   Gurnani Hiren   "
print(x.strip())
x="Geeks for Geeks For Geeks for Geeks"
print(x.strip("Geeks"))
x="The king has the largest army in the world The"
print(x.strip("The"))


#Join Method in Python.
x='c'           #List tupple sets dictionary in iterable string forms if in int form L=[1,2,3] will throw error.
x=x.join(['a','t'])
print(x)
x="Geeks"
List=['1','2','3','4']
x=x.join(List)
print(x)
x="".join(('h','i','r','e','n'))
print(x)
x="".join(("Gurnani","Hiren","Anilbhai"))
print(x)
x="_".join({'g':1,'e':2,'e':3,'k':4})
print(x)
#Encoding in Pythons
#encode(encoding,error)
string="Gurnani"
print(string.encode())
print(string.encode('utf8','namereplace'))
string="Waheguru"
print(string.encode('ascii','replace'))
string="sls"
print(string.encode('ascii','Hiren'))


x="Gurnan#Hiren#AnilBhai#sls#Product"
print(x.split('#',-10))
print(x.split('#',-1))
print(x.split('#',-20))