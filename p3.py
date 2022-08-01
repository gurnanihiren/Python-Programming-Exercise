
#Write a program to add Numbers between 1 to n.

n=int(input('Enter a value for n:'))
sum1=0
for i in range(1,n+1):
    sum1=sum1+i        
        
print(f'Sum of values from 1 to upto {n} is {sum1}')       