#Namespace and scope of Variables IN Python.

print('Local namespace')
count=0
def count_values_local():

    count=12        #priority will be given to Local.
    count=count+1
    print(f"count in local_namespace{count}")

print(f"count in global_namespace{count}")
count_values_local()        #Calling Function

print('Global Namespace')
count=0
def count_values_global():
    global count
    count=12
    count=count+1
    print(f"count is {count}")

count_values_global()

#A class is a user defined data type.
#A class have attributes(name,breed,age) and behaviour that is Functions.
#A class can have n number of objects.Creating class Objects are called instantiation of class.

class Hiren:
    pass

    
class college():
    name="Hiren"
    age=23

    def details(self):
        print(f'My name is {self.name}:')
        print(f"My age is {self.age}:")


x=college()
print(x.name)
print(x.age)
print(college.name)
print(college.age)
x.details()


#To Understand use of self.
#Creating Multiple Objects of same class

class Laptop():
    def details(self):
        self.company=input('Enter the name of the Company:')
        self.model_no=input('Enter Model No:')
        print(f'Laptop company name is {self.company}')
        print(f'Model No is {self.model_no}')
        
x=Laptop()
x.details()
y=Laptop()
y.details()
z=Laptop()
z.details()  


#Constructor in Python.     #Without self it will throw an error in argument.
class details():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def printing_details(self):
        print(f'name of person is {self.name}')
        print(f'age of person is {self.age}')

x=details("Hiren",23)
#x=details()
x.printing_details()


#Any name of self can be taken.

class details():
    def __init__(abc_as_self,str):
        abc_as_self.str=str
        print(abc_as_self.str)

x=details("SLS is a product based Company")


#Creating Object 2 from Object 1 class

class first():
    def __init__(self):
        self.fst=second()
    def printing_details(self):
        print('This is First class')

class second():
    def printing_details(self):
        print('This is second class')

object1=first()
object2=object1.fst                 #Assigning class to another object as object of first class.
object1.printing_details()
object2.printing_details()


#Multiple Instances of a class with Constructor.

class coffee():
    str="CoffeDetails"    
    def __init__(self,coffee_name,coffee_price):
        self.coffee_name=coffee_name
        self.coffee_price=coffee_price

    def printing_details_of_coffee(self):
        print(f"Coffee name is {self.coffee_name}")
        print(f"Coffee price is {self.coffee_price}")

coffee1=coffee("Espresso","2.71")
coffee2=coffee("Latte","2.61")
print(coffee1.str)
coffee1.printing_details_of_coffee()
print(coffee2.str)
coffee2.printing_details_of_coffee()

#Inheritance in class
#Single Inheritance

class person():
    def __init__(self,name):
        self.name=name

    def get_person_identity(self):
        return self.name
    
    def isemployee(self):
        return False

class child(person):
    def isemployee(self):
        return True
    

x=person("Gurnani Hiren")
print(x.get_person_identity(),x.isemployee())
x=child("Gurnani Hiren")
print(x.get_person_identity(),x.isemployee())


#Program to demonstrate issubclass or derived class

class Base():
    pass

class child(Base):
    pass

print(issubclass(Base,child))
print(issubclass(child,Base))

x=Base()
y=child()

print(isinstance(x,Base))
print(isinstance(y,child))


#Inheritance(Multiple Inheritance)with constructor inheritance.

class person1():
    def __init__(self,name,gender,age):
       self.x=name
       self.y=gender
       self.z=age
       print('person1')
class person2():
    def __init__(self,name,gender,age):
        self.a=name
        self.b=gender
        self.c=age
        print('person2')

class person3(person1,person2):

    def __init__(self):                              #Most Important to inherit parents constructor also
        person1.__init__(self,"Anil","Male",55)     #Most important to pass value or else will Throw error.
        person2.__init__(self,"Renu","Female",45)
        print('person3')
    def details(self):
        print(self.x)
        print(self.y)
        print(self.z)
        print(self.a)
        print(self.b)
        print(self.c)


random=person3()
random.details()

#Inheritance#Multilevel Inheritance

class grandparent():
    def __init__(self,x):
        self.a=x
        print('This is grandparent class')

class father(grandparent):
    def __init__(self,y):
        self.b=y    
        print('This is a parent class')


class child(father):
    def __init__(self):
        grandparent.__init__(self,10)
        father.__init__(self,20)
        self.c=self.a+self.b
        print('This is a child class')
    def details(self):
        print(f"Addition of two Numbers is {self.c}")

y=child()
y.details()

#Heirarical inheritance in Python

class parent():
    def func1(self):
        print('This is parent class')

class child1(parent):
    def func2(self):
        print('This is child1 class')

class child2(parent):
    def func3(self):
        print('This is child2 class')

x=child1()
x.func1()
x.func2()
y=child2()
y.func1()
y.func3()



