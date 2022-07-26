
print('String Encode Method in Python')
string=input('Enter a string:')

from encodings.aliases import aliases
print(aliases.keys())

print(string.encode())
print(f'Encoding in utf-8 and ignore error is {string.encode("utf-8","ignore")}')
print(f'Encoding in ascii and replace is {string.encode("ascii","replace")}')
print(f'Encoding in ascii and ignore is {string.encode("ascii","ignore")}')
print(f'Encoding in utf-8 and namerplace is {string.encode("utf-8","namereplace")}')
print(f'Encoding in utf-8 and ignore is {string.encode("utf-8","ignore")}')
print(f'Original string is {string}')

print('String Format Method in Python-Keyword Argument.')
string="My name is {name}.My age is {age}"
print(string.format(name="Hiren",age=23))
string="{company} is a {sector} based Company"
print(string.format(company="sls",sector="Product",name="GG"))
#string="{company} is a {sector} based Company {}"
#print(string.format(company="sls",sector="Product","SLS"))         #positional Argument follows Optional Argument.  
#print(string.format("sls","product"))

print('Index Method in Python in string Formatting.')
string="{} is {} based Company"
print(string.format("sls","Product"))
#print(string.format("sls"))-Index Error
print(string.format("sls","Product","Hiren"))

print('Join Method in string in Python')
string=""
print(string.join(['1','2','3','4']))
string="Gurnani"
print(string.join(['H','I','R','E','N']))
string="_"
print(string.join(('1',"hiren",'2',"Waheguru")))
string=' '
print(string.join({'1','sls','1-0'}))
string=' '
print(string.join({'1':'Gurnani','2':'Waheguru'}))
#print(string.join({1:'Gurnani',2:'Waheguru'}))
string=""
#print(string.join(None))
print(string.join('1'))

print('strip Method in Python')
string="Gurnani Hiren"  
print(string.strip())
string="   Gurnani Hiren   "
print(string.strip())
string="nGurnani Hiren"
print(string.strip("n"))
string=" nGurnani Hiren "
print(string.strip())
string="The sun rises in the east The"
print(string.strip("The"))
print(string.strip("the"))
string="sls is a product based company sls"
print(string.strip("sls"))
string=" sls is a product based company sls "
print(string.strip("sls"))
string="SLS is a product based company sls"
print(string.strip("SLS"))
print(string.strip(None))

print('split Method in Python')
x="Gurnani          Hiren"
print(x.split())
x="Gurnani####Hiren####Anilbhai"
print(x.split('#'))
x="Gurnani##Hiren##Anilbhai"
print(x.split('####'))
x="Gurnani$rrHiren"
print(x.split('$'))
x="Gurnani$Hiren$Anilbhai$sls"
print(x.split('$')) #Default -1 all split
print(x.split('$',0))   #Returns 1
print(x.split('$',-12)) #same as default
print(x.split('$',1))
#print(x.split(None,None))

print('splitness Method in Python')
#0-represents True.
#positive/Negative represents False.
string="\nGurnani \n\n\nHiren\n"
print(string.splitlines(True))
print(string.splitlines(False))
string="sls \n is \n a product \n based company"
print(string.splitlines(True))
print(string.splitlines(False))


