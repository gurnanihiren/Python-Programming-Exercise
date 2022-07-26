'''
print('String Indexing in python.')
string=input('Enter a string:')
print(string[0])
print(string[1])
#print(string[9])       #if index is not accessible will throw Error Index out of range.
print(string[-1])
#print(string[-10])

print('String slicing in python.')
string=input('Enter a string:')
print(string[:])
print(string[1:4])
print(string[:3])
print(string[2:])
print(string[9:14])     #if string small will print Nothing and will not throw Error.
print(string[::-1])     #Will print in Reverse.
print(string[:-1])
print(string[-6:-2])
print(string[2:6])      #Reverse indexing not possible but will not throw error and prints nothing.
print(string[-2:-6])
print(string[::-100])
print(string[::-10])    #undefined behaviout.
print(string[::47])

print('string Functions in Python.')
string=input('Enter a string:')
print(string.lower())
print(string.upper())
print(string.capitalize())

print('string_count_Function in Python.')
string=input('Enter a string:')
print(string.count('Gurnani'))
print(string.count('n'))
print(string.count('i'))
print(string.count('Hiren'))
#print(string.count(1)) #Must be str not int
#print(string.count(None))#Must be str not Nonetype

print('string_index Function in Python.')   #Case sensitive
string=input('Enter a string:')
print(string.index('nani'))
print(string.index('n'))
#print(string.index('n',0,3))
print(string.index('n',1,5))
#print(string.index('nani',-1,-5))          #Reverse Indexing returns index Error
print(string.index('n',-5,-1))


print('Find_string Method in Python')   #Case sensitive
string=input('Enter a string:')
print(string.find('nani'))
#print(string.find('nani',0,5))         -dOES NOT returns error but returns -1 vALUE
print(string.find('nani',0,8))
print(string.find('urn'))
print(string.find('n'))
#print(string.find('nani',8,0))
#print(string.find('nani',-6,-1))   Reverse Indexing returns -1.
#print(string.find('nani',-1,-6))
'''
print('Replace string_Function in string.')
#if string not found returns original string
#if negative value found than also returns original string.
string=input('Enter a string:')
print(string.replace('Geeks','geeks'))   #Enter unknown value original string will return.
print(string.replace(string,'Nevada'))
print(string.replace('nani','ekgs',2))
print(string.replace('nani','ekgs',0)) #replaces all   #both the argument must be str or type error.
#print(string.replace(None,None,10))G

print('string split in Python.')
string="Gurnani Hiren"
print(string.split(' '))     #if seperator without space returns empty seperator Error.by default value -1.
string="Gurnani#Hiren#Anilbhai"
print(string.split('#',1))
string="Gurnani####Hiren##Anilbhai"
print(string.split('$'))    #Returns Original string in List.if different seperator provided.
print(string.split('####'))
string="gurnaniHirenGurnaniAnilbhai"    #Case senisitive.
print(string.split("Gurnani"))
string="$GurnaniHiren$"
print(string.split('$'))
string="sls is a product based Company"
print(string.split(None,-10))    #if none and negative value provided returns original
                                 #Max split should be integer only
print(string.split(None))



#strip([chars])
print('String strip Function')
string=input('Enter a string:')
print(string.strip())
string="The lord is present everywhere The"
print(string.strip("The"))
string="lord is present everywhere The"
print(string.strip("The"))
string="Geeks for Geeks"
print(string.strip(None))   #Returns Original.
string="GeeksforGeeks"
print(string.strip("Geeks"))
string="Waheguru"   #if substring not Found returns original
print(string.strip('The'))


print('Encoding in Python')
#encoding_scheme,Error
string="Gurnani Hiren"
#print(string.encode('utf-8',None))
string="Gurnani Hiren"
print(string.encode('ascii','ignore'))
#print(string.encode('utf-8',''))
string="Gurnani Hiren"
print(string.encode('utf-8','replace'))
string="Gurnani Hiren"
print(string.encode('ascii',"Hiren"))

print('Join Function in string')    #Accepts only string sequence.
string=""
print(string.join(['1','2']))
string="Cat"
print(string.join('Waheguru'))
string=""
#print(string.join('cat','bat','sat')) Takes only one argument.
y=('cat','bat','rat')
print(string.join(y))
#string="GurnaniHiren"
#print(string.join(None))

y={'Hiren':'Gurnani','Waheguru':'Hiren'}
print(string.join(y))

print('Format in string')
#Value in Format is character,floating,string,integer.
string="{} is 23 years old"
print(string.format("Hiren"))
string="{} {} is {} years old"
print(string.format("Gurnani","Hiren",23))

string="{1} {0} is {2} years old"
print(string.format("Hiren","Gurnani",23))
#string="{0} {1} is {3} years old"  -Index Out of range.
#print(string.format("Gurnani","Hiern",23))

print('string splitness in Python')
string="Gurnani\nHiren\nWaheguru\n"
print(string.splitlines(True))
print(string.splitlines(0))
print(string.splitlines(3))
print(string.splitlines(-1))
print(string.splitlines(False))
#print(string.splitlines(None))
#print(string.splitlines("Gurnani"))