import sys
#1. Write python function which takes a variable number of arguments.

def myfuntion(*var):
    print(var)

myfuntion(1,3,6)

# 2. WAP (Write a program) which takes a sequence of numbers and check if all numbers are unique.

def check_distinct(datalist):
    if len(datalist) == len(set(datalist)):
        return True
    else:
        return False

print(check_distinct([2,3,4]))

# 2.1. Write a program for counting the number of every character of a given text file?

#3. Write a program to print the given number is odd or even.
n = [2, 1, 4, 3, 7]

for i in n:
    if i%2 == 0:
        print('even numbers:', i)
    else: 
        print('odd numbers:', i)
        
#4. Write a program to find the given number is positive or negative.
n = [-2, 1, -4, 3, 7, 0]
for i in n:
    if i < 0:
        print('negative numbers:', i)
    else: 
        print('positive numbers:', i)

#5. Write a program to find the sum of two numbers.
a=4
b=9
size=sys.getsizeof(b)
print(size)
print(a+b)

#6. how can check the variable size
b=9
size=sys.getsizeof(b) #bytes

#7. Write a program to find if the given number is prime or not.
