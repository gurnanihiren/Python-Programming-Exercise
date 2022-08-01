
#Write a python Program to count Number of digits in a Number.
#75869 #No of digits = number of remainders in a Number
number=int(input('Enter a Number:'))
count_digits=0
if number == 0:
    count_digits=count_digits+1
    print(f'Total Number of digits in a Number are {count_digits}')
else:
    while number>0:
        count_digits=count_digits+1
        number=number//10    
    print(f'Total Number of digits in a Number are {count_digits}')







