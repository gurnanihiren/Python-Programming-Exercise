

print('Opening File in Python')

#file_object=open('example_1.txt','r')  #if file does not exist it will throw error
file_object=open('example_1.txt','w')    #File Created

print('Closing File in Python')
file_object.close()

print('File-Operations(write) in python')
file_object=open('example.txt','w')
file_object.write('Gurnani-Hiren')
file_object.write('sls is a product based Company')
file_object.close()

print('File-Operations(Read) in Python')
file_object=open('example.txt','r')
#data=file_object.readline()

data=file_object.readline()
print(data)

file_object.close()
print('File-operation(Append) in Python')
file_object=open('example.txt','a')
file_object.write('Sun rises in the east and sets in the west')
file_object.close()


print('Printing Appended Data')
file_object=open('example.txt','r')
data=file_object.readline()
print(data)
file_object.close()

