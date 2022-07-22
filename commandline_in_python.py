

#print(['.\\commandline_in_python.py', '2', '3', 'next.txt', 'r', 'a' 'w'])
print('Command Line Argument in Python')
import sys
print(sys.argv[:])
print(sys.argv[0])
print(f'Total number of arguments using command Line are {len(sys.argv)}')

print('Example-1')
print('_________')
try:
    if(len(sys.argv) < 2):
        print('Less Number of Inputs in Command Line')
    else:
        c = int(sys.argv[1]) + int(sys.argv[2]) 
        print(f'Addition of two values is {c}') 
except ValueError:
    print('Cannot Convert data to Int')


print('Example-2')
print('_________')
try:
    file=open(sys.argv[3],sys.argv[4])
    file.write('Opened in Write Mode')
    file.close()
    file=open(sys.argv[3],sys.argv[6])
    data=file.read()
    print(f'Data in File is {data}')
    file.close()
except FileNotFoundError:
    print('Unable to Open File,File does not exists')
except IndexError:
    print('List Index Out of range please provide Arguments')
except ValueError:
    print('Cannot Convert to int data type')
    
print('Example-3')
print('_________')
try:
  #  print('Enter data Through Command Line arguments')
    file=open(sys.argv[3],sys.argv[5])
    file.write("Opened in Append Mode")
    file.close()
    file=open(sys.argv[3],sys.argv[6])
    data=file.read()
    print(f'Data in file is {data}')
    file.close()
except IndexError:
    print('List Out of range please provide Argument.')
except ValueError:
    print('Cannot Convert to int data type')


#if unable to access sys arguments will throw Error
print('Example-4')
print('_________')
try:
    file=open(sys.argv[3],sys.argv[6])
    data=file.readlines()
    print(f'Data in File is {data}')
    file.close()
except IndexError:
    print('List Out of range please provide Arguments')
except FileNotFoundError:
    print('Unable to Open File,File does not exists')
except ValueError:
    print('Cannot Convert to int data type')

import os
x=os.getcwd()
print(f'Current Working Directory is {x}')
os.chdir('E:\Local\Desktop\pythonprograms\os_module')
x=os.getcwd()
print(x)
print('Make directory using os')
try:
    os.mkdir('E:\Local\Desktop\pythonprograms\Hiren')
except FileExistsError:
    print('File Exist Error')

try:
    os.mkdir('E:\Local\Desktop\pythonprograms\Waheguru')
except FileExistsError:
    print('File Exist Error')

os.rmdir('E:\Local\Desktop\pythonprograms\Hiren')
os.rmdir('E:\Local\Desktop\pythonprograms\Waheguru')

try:
    os.rename('E:\Local\Desktop\pythonprograms\Hiren','E:\Local\Desktop\pythonprograms\Hiren_1')
except FileNotFoundError:
    print('Cannot Find Specified Folder')


print('Another example of commandLine argument')

try:
    n1=int(input('Enter a value for n1'))
    n2=int(input('Enter a value for n2'))
except NameError:
    print('Invalid Input for type Integer.')
except ValueError:
    print('Invalid Input for integer')
else:
    print('Exception did not Occur so Running Else clause.')
finally:
    print('I am always going to run.')


x=int(input('Enter a value of x:'))
try:
    print(x/0)
except ValueError:
    print('Invalid input for string')
except ZeroDivisionError:
    print('Number cannot be divided by Zero')

try:
    raise keyboardInterrupt
finally:
    print('I will always Run')

    

    
