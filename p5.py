
#list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
#Write a program to iterate through List and break the List if >150

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for i in list1:
    if i % 5 == 0 and i < 150:
        print(i,end=" ")
    else:
        pass
print()


for i in list1:
    if i % 5 == 0:
        if i < 150:
            print(i,end=" ")
        else:
            break
    else:
        pass