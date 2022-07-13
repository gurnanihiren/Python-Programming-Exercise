#Rules for Identifier

#54fkgdgk=5     Does not start with a Number.
#print(54fkgdgk)

#global=1   Does not start with a built in keyword.
#print(global)

#adf$%=14   Does not contain a special character.
#print(adf$)


site="gfg"
if site == "gfg":
    print("Logging You on screen")
else:
    print("Invalid syntax")
    
'''
Multi Line Comments
jFRJKENFRJFN
frmjedlfvg
'''

#This is a single Line Comment.


def multiply(a,b):
    print(a*b)
    
multiply(1,2)
multiply(4,4)
multiply(5,10)

#Quotations In python.
var='Hiren'
print(var)
var="Hiren"
print(var)
var='''Hiren'''
print(var)

'''
mov="hiren'
print(mov)
mov='harsh"
print(mov)
'''

print("It's a bad example")
print('she said,"Thankyou!"')
print('It\'s Hot today')    

print('''she said,"Thankyou!"''')
#print("""she said,"Thankyou!"""")

print("Printing All List")
import keyword
print(f"List in Python is {keyword.kwlist}")

count=0
for i in keyword.kwlist:
    count=count+1
print(f"Total No of Keywords in List is {count}")

print("""This is a world where "No one cares" """ )

print("""She said, "Thank you! It's mine." """)

print('''She said, "Thank you! It's mine."''')

print("Multi Line comments")
print("Explicit Multi Line")
print([1, \
    2, \
    3, \
    4, \
    ])
    
    
    
print(["Gurnani",\
"Hiren", \
"Waheguru", \
"Ikonar",\
])
print("Implicit Multi Line Comment")
print([1,
2,
3,4,
5])
