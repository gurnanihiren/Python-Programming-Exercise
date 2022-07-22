
print('Few of exceptions in python.')
print('____________________________')
print('Zero Division Error:Exception')
#print(1/0)
print('Name Error defined:Exception')
#print(a+b)
print('Type Error Based Exception.')
#print(1+"Gurnani")

print('Handling Exceptions -Example1')

#while True:
try:
    x=int(input('Enter a value:'))
        #break
except ZeroDivisionError:
    print('Number Cannot be Divided by zero.')
except TypeError:
    print('Invalid Input of type str or Floating type.')
except NameError:
    print('Variavle x is not defined.')
except ValueError:
    #raise ValueError
    print('Invalid Literal for int input')
else:
    print('Exception didnt occur so running else clause')

print('Handling Expections -Example2')
print('_____________________________')

def divide_by_zero(value1,value2):
    print(value1/value2)

while True:
    try:
        value1=int(input('Enter a value 1:'))
        value2=int(input('Enter a value 2:'))
        break
    except ValueError as err:
        print('Invalid Input for Value1 and Value 2',err)

#while True:
try:
    divide_by_zero(value1,value2)
    #break
except ZeroDivisionError as error:
    print('Value cannot be divide by zero',error)
except TypeError as error:
    print('Unmatched Type for Division',error)
except ValueError as error:
    print('Invalid Output with different input - string',error)
else:
    print('Exception didnt raise so running else.')
finally:
    print('Regardless Running.')

try:
    raise ValueError
except ValueError:
    print('Value Error Exception is Printed!')
else:
    print('In else clause')
finally:
    print('In Final Clause')
#else:
#    print('Executing else clause')
                                                    
try:
    raise ZeroDivisionError
except ZeroDivisionError:
    print('Zero Division Error is Printed')
finally:
    print('Waheguru')
#except ZeroDivisionError:
#    print('ZeroDivisionError Raised using try')


print('Try-Finally Clause Exception in Python Example-1')
print('______________________________________')

while True:
    try:
        x=int(input('Enter a value:'))
        break
    except ValueError:
       print('Different Type of data.')
    except ZeroDivisionError:
        print('Divide by zero error.')
    finally:
        print('Hello World')

print('Try-Finally Clause Exception in Python Example-2')

def print_details():
    try:
        return False
    finally:
        return True

x=print_details()
print(x)
'''
print('Handling Expections - Example3')
try:
    for i in sys.argv[1:]:
        file=open(i,'r')
        print(file.readline())
    except OSError as err:
        print('Cannot Open argv File',err)
  #  except 
'''


#Notes
#Else occurs if exception does not occurs.if user right exception values and if it does not encounter else will print.
#Finally will work regardless of any exception working or not.
