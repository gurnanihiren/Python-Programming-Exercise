
#List Compression in Python is Given by
#newList = [ expression(element) for element in oldList if condition ] 
#List Compression returns List

List=[]
for characters in "Gurnani Hiren":
    List.append(characters)

print(List)

List=["Gurnani Hiren Anilbhai","Waheguru ji"]
new_List=[]
for i in range(len(List)):
    string=str(List[i])
    print(string)
    for i in string:
        if i == " ":
            pass
        else:
            new_List.append(i)

print(f"New List is {new_List}")

#List Compression in Python

x=[i**2 for i in range(10)]
print(x)

x=[1,2,3,4,5,6,7,8,9,10]
y=[i for i in x if i % 2 == 0]
print(y)

string=[string[::-1] for string in ("Geeks","Waheguru")]
print(string)
x=[x[::-1] for x in ["Waheguru","Gurnani","Hiren","Mona"]]
print(x)


#Using Function Defination.
def digitSum(n):
    sum=0
    while(n!=0): 
        remainder=n%10
        sum=sum*10+remainder
        n=n//10
    return sum


List=[357,457,654]
for i in range(len(List)):
    x=digitSum(List[i])
    print(x)

List=[342,543,654]
#L=[print(i) for i in List]
#Using List Compression.
L=[digitSum(i) for i in List]
print(L)


#2d List in Python
List=[[1,2],[3,4],[5,6],[7,8]]
print((List[0][1]))             #Accessing List elements individual in 2d List
print((List[0][0]))             #Accessing List elements
print((List[0]))                #Accessing individual List element subset of two elements.


#List=[[1,2,3,4,5],
#[6,7,8,9,10],
#[11,12,13,14,15]
#[16,17,18,19,20]
#[21,22,23,24,25]
List=[]
for i in range(5):
    List.append([])
    if i == 0:
        for j in range(0,6):
            List[i].append(j)
    if i == 1:
        for j in range(6,11):
            List[i].append(j)
    if i==2:
        for j in range(11,16):
            List[i].append(j)
    if i==3:
        for j in range(16,21):
            List[i].append(j)
    if i==4:
        for j in range(21,26):
            List[i].append(j)

print(List)

#List=[[1,2,3,4,5],
#[6,7,8,9,10],
#[11,12,13,14,15]
#[16,17,18,19,20]
#[21,22,23,24,25]
#Creating same List which is above using List Compression.
x=[]
for i in range(5):
    if i == 0:
        x.append([j for j in range(0,6)])   #ListCompression.
    elif i == 1:
        x.append([j for j in range(6,11)])  #ListCompression.
    elif i == 2:
        x.append([j for j in range(11,16)]) #ListCompression.
    elif i == 3:
        x.append([j for j in range(16,21)]) #ListCompression.
    elif i == 4:
        x.append([j for j in range(21,26)]) #ListCompression.
    else:
        pass

print(x)

'''
#L=[[1,2,3],[4,5,6],[7,8,9]]
#L=[[1,2],[3,4],[5,6],[7,8]] #4x2---2X4
L=[[1,2,3],[5,6,7],[44,33,22]]
#Transpose of a Matrix is L=[1,4,7],[2,5,8],[3,6,9]]
x=[]
k=0
for i in range(len(L)):    
    x.append([])
    for j in range(len(L[i])):      
        x[i].append(L[j][k])
    k=k+1

print(f"Transpose of the Given List is {x}",end="\n")
'''