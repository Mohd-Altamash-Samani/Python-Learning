# Write a python Code to print the Hello Wolrd

print("Hello Wolrd!")

# Write a program to print Twinkle twinkle little star poem in python.

print(""" Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in themarkssky """)

# Write a python code to do arithmetic operation

# Addition
a=float(input("Enter the fisrt no."))
b=float(input("enter the second no."))
print(f"sum of {a} + {b} = {a+b}")

# Division
if b==0:
    print("Division by 0 is not allowed")
else:
    print(f"division of {a} / {b} = {a/b}")

# print the table of users interest

n=int(input("enter the number"))
for i in range(1,11):
    print(f"{n}*{i} =",i*n)    
    
# Write python code to swap a two number

a=int(input("Enter the number"))
b=int(input("Enter the number"))
print(f"the orginal no is {a},{b}")
temp=a
a=b
b=temp
print(f"after swapping the no. is {a},{b}")

# OR

a,b=b,a
print(f"after swapping the no. is {a},{b}")

# OR

a=8
b=5
a=a+b
b=a-b
a=a-b
print(f"after swapping the no. is {a},{b}")

# To generate a random number

import random
print(f"the random are {random.randint(1,100)}")

total=10
data=[random.randint(1,20) for _ in range(total)]
print(data)

# to display the calender

import calendar
year=int(input("enter the year:"))
month=int(input("enter the month:"))
cal=calendar.month(year,month)
print(cal)

# Solve the quadratic equation

import math
# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
# Calculate the discriminant
discriminant = b**2 - 4*a*c
# Check if the discriminant is positive, negative, or zero
if discriminant > 0:
 # Two real and distinct roots
 root1 = (-b + math.sqrt(discriminant)) / (2*a)
 root2 = (-b - math.sqrt(discriminant)) / (2*a)
 print(f"Root 1: {root1}")
 print(f"Root 2: {root2}")
elif discriminant == 0:
 # One real root (repeated)
 root = -b / (2*a)
 print(f"Root: {root}")
else:
 # Complex roots
 real_part = -b / (2*a)
 imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
 print(f"Root 1: {real_part} + {imaginary_part}i")
 print(f"Root 2: {real_part} - {imaginary_part}i")

# to find odd or even number and positive negative or zero

num=float(input("Enter the number"))

if num>0:
    print("the number is positive")
elif num==0:
    print("the number is zero")
else :
    print("the number is Negative")
    
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")
    
# Write a Python program to print even numbers in a list

number=[3,4,5,3,3,4,5,76,4,32]
#Using List Comprehension
even=[num for num in number if num%2==0]
even

# using list comprehensions, create a function that finds all even numbers from 1 to the given number.

def find_even_nums(num):
 return [x for x in range(1, num + 1) if x % 2 == 0]

find_even_nums(20)    


# find the leap year or not

year=int(input("neter the year"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year")
else:
    print("The year is not a leap year")

    
# whether a number is a prime or not   

num=int(input("Enter the number")) 

flag=True
if num==1:
    print(f"the {num} the is not a prime number")
elif num>1:
    for i in range(2,num):
        if(num%i==0):
            flag=False
            break
if flag==True:
    print(f"the {num} is a prime number")
else:
    print(f"the {num} is not a prime")
    
# Print prime numbers between 1 and 20

for i in range(2, 21):
    is_prime = True  
    for j in range(2, int(i**0.5) + 1): 
        if i % j == 0: 
            is_prime = False
            break
    if is_prime:
        print(i)

        
# Write a Python Program to Find the Factorial of a Number

num=int(input("enter the number"))
fact=1

for i in range(1,num+1):
    fact=fact*i
print(fact)  

# Write a Python Program to Find the Factorial of Number Using Recursion.

def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

num=int(input("enter the number"))

print(fact(num))   

# Write a Python Program to Print the Fibonacci sequence

num1=0
num2=1

print(num1)
print(num2)
 
for i in range(1,11):
    n=num1+num2
    print(n)
    num1=num2
    num2=n

# Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal.

dec_num = int(input('Enter a decimal number: '))
print("The decimal value of", dec_num, "is:")
print(bin(dec_num), "in binary.")
print(oct(dec_num), "in octal.")
print(hex(dec_num), "in hexadecimal.")

# Get ASCII value of a single digit
num = 5
print(f"The ASCII value of {num} is {ord(str(num))}")

# Get ASCII value of a single character
char = 'A'
print(f"The ASCII value of '{char}' is {ord(char)}") 
                 
# Write a Python Program to calculate the natural logarithm of any number.    
    
import math
num = float(input("Enter a number: "))
if num <= 0:
 print("Please enter a positive number.")
else:
 result = math.log(num)
 print(f"The natural logarithm of {num} is: {result}")


# Write a Python Program for cube sum of first n natural numbers?

def cube_fun(n):
    total=0
    for i in range(1,n+1):
       cube=i**3
       total=cube+total
    print(total)
cube_fun(7)  

# Write a Python Program to find the largest element in an array.

def max_fun(arr):
    maximum = arr[0]
    for i in arr:
        if i > maximum:
            maximum = i
    return maximum   

arr = [12, 5, 89, 23, 45]
print("The largest element is:", max_fun(arr))

# Write a Python program to find N largest elements from a list.

def n_largest(num,n):
    sort=sorted(num,reverse=True)
    save=sort[:n]
    return save

num=[3,4,5,3,3,4,5,76,4,32]
n=3

n_largest(num,n)

# Write a Python Program to Remove Punctuation From a String.

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = input("Enter a string: ")
no_punct = ""
for char in my_str:
 if char not in punctuations:
  no_punct = no_punct + char
print(no_punct)


# A Disarium number is a number that is equal to the sum of its 
# digits each raised to the power of its respective position. For example, 
# 89 is a Disarium number because 8 + 81 = 89.

#A Happy Number is a positive integer that, when you repeatedly replace
# the number by the sum of the squares of its digits and continue the process, eventually reaches 1. 
# If the process never reaches 1 but instead loops endlessly in a cycle, the number is not a Happy Number eg. 19

# A Harshad number (or Niven number) is an integer that is divisible by the sum of its digits.
# 18 is a Harshad number because , and 18 is divisible by 9
# 46 is not a Harshad number because , and 46 is not divisible by 6.


# Write a Python program to Remove empty List from List.

list_of_lists = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]
filtered_list = [i for i in list_of_lists if i]
print("List after removing empty lists:", filtered_list)

input_str = "Python program to split and join a string"
word_list = input_str.split() 
print(word_list)
output_str = " ".join(word_list)
print(output_str)

# Write a Python program to find uncommon words from two Strings

def uncommon_words(str1, str2):
 words1 = set(str1.split())
 words2 = set(str2.split())
 uncommon_words_set = words1.symmetric_difference(words2)
 uncommon_words_list = list(uncommon_words_set)
 return uncommon_words_list

string1 = "This is the first string"
string2 = "This is the second string"
uncommon = uncommon_words(string1, string2)
print("Uncommon words:", uncommon)

# Write a Python program to Merging two Dictionaries.

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1)

# Write a program to check the validity of password input by users

import re

def is_valid_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    
    if not (re.search("[a-z]", password) and
            re.search("[0-9]", password) and
            re.search("[A-Z]", password) and
            re.search("[$#@]", password)):
        return False
    
    return True

password_input = input("Enter your password: ")

if is_valid_password(password_input):
    print("Password is valid.")
else:
    print("Password is not valid. Please make sure it meets the specified criteria.")


# Create a function that sorts a list and removes all duplicate items from it.

def sort_rem(lst):
    return sorted(set(lst))

result = sort_rem([22, 3, 34, 5, 3, 3, 22])
print(result)

# Let's See some Programming jokes.

# pip install pyjokes
import pyjokes
print(pyjokes.get_joke())

# Install an external module and use it to perform an operation of your interest. 

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello, i am altamash!! what do you want you here from me ? ")
engine.runAndWait()

# Write a python program to find remainder when a number is divided.

def remainder(a,b):
    remain=a%b
    print(remain)

number1=int(input("dividend"))
number2=int(input("divisor"))
remainder(number1,number2)

# Escape sequence character 
string = "Altamash is good in 'sports'\nbut he also\t loves to study \"all-rounder\""
print(string)

# Write a program to fill in a letter template given below with name and date.

letter = '''Dear <|Name|>,
You have been selected!
<|Date|>'''
print(letter.replace("<|Name|>","Manish").replace("<|Date|>",'04-sep-2024'))

# Write a program to detect double space in a string.

name = "What was the name of our class teacher"
print(name.find("  "))

name = "What was the  name of our class teacher"
print(name.find("  "))

# charactersitics of tuple
a=(1)
b=(1,)
print(type(a))
print(type(b))

tuple=(3,9,6,10)
a, b, c, d=tuple
print(a,b,c,d)
print(type(a))

# Write a program to store 3 fruits in a list entered by the user

fruit_list=[]
for i in range(0,3):
    enter=input("enter the fruit name :-")
    fruit_list.append(enter)
print(fruit_list)    

# Write a program to accept marks of 6 students and display them in a sorted manner.

list=[]
for i in range(0,3):
    enter=int(input("enter the marks: "))
    list.append(enter)

list.sort()    
print(list)   

# Count the number of the zeros
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))
print(sum(a))

# Dictionary
marks = {
"key": "value",
"samani": "code",
"marks": "100",
"list": [1, 2, 9]
}

print(marks['samani']) # return an error when not found
print(marks.get('samani')) # returns a None when not found

print(marks.items())
print(marks.keys())
print(marks.values())

# Define

a = "" # empty string
b = [] # empty list
c = () # empty tuple
d = {} # empty dictionary
e = set() # empty set

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# . Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

d={}
for i in range(0,2):
    key=input("enter the key")
    value=input("enter the value")
    d.update({key:value})
    # d[key]=value
print(d)     

# Write a program to find out whether a student has passed or failed if it requires a total of 40% and
# at least 33% in each subject to pass. Assume 3 subjects, 10 marks each and take marks as an input from the user.

marks=[]
for i in range(0,3):
    mks=int(input("enter the marks"))
    marks.append(mks)

if (sum(marks)/30)*100 >= 40 and 33 <= (marks[0]/10)*100 and 33 <= (marks[1]/10)*100 and 33 <= (marks[2]/10)*100:
    print("passed")
else:
    print("failed")

'''
*
**
*** for n=3
'''  
n=10
for i in range(1,n):
    print("*"*i)

'''
  *
 ***
***** for n = 3
'''    
n=10
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1))

'''
* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *   
'''
n=5
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*(i))

for i in range(2,n+1):
    print(" "*(n-i)+"* "*(i))

# Write a python function to remove a given word from a list ad strip it at the same time

l=["   altamash"," husain","adil  "," manish "]
strip=[element.strip() for element in l]
print(strip) 

# OR

def rem(l, word=None):
    list=[]
    for i in l:
      if word is not None:
          i=i.replace(word,"") 
      i=i.strip()
      list.append(i)
    return list
l=["   altamash"," husain","adil  "," manish "]
output=rem(l,"a")
print(output)

str="Hey it's been a while since we met."
f=open("write.txt","w")
open=f.write(str)
f.close()

with open("write.txt","r") as f:
    print(f.read())

# Write a program to read the text and find out whether it contains the word ‘twinkle’.

with open("write.txt","r") as f:
    read=f.read()
    if "Twinkle" in read:
        print("twinke is present in the file")
    else:
        print("twinkle is not present in the file ")    

# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.

def table(n):
    table=""
    for i in range(1,11):
        table+=f"{n} X {i} = {n*i}\n"
    with open(f"table{n}.txt","w") as f:
        f.write(table)

for i in range(2,3):
    table(i) 

# Walrus Operator 

results = [square for value in range(10) if (square := value ** 2) > 30]
print(results)      

# Oops (dry principle)

class employee:
    skills="Statistics"
    role="intern"

    def getinfo(self):
        print(f"The skill of the employee is {self.skills} and role is {self.role}")
     
    @staticmethod  # also called as decorator 
    def greed():
        print("Hi Sir, Good Morning :") 

    def __init__(self):  # dunder method beacuse of __
        print("You will see this everytime you call the class employee")



altamash=employee()
altamash.skills="data analyst"
altamash.getinfo()  # OR employee.getinfo(altamash)
altamash.greed()

# . Create a class “Programmer” for storing information of few programmers working at Microsoft.

class programmer:
    company="Microsoft"

    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

a=programmer("altamash",1200000,400601)
print(a.company,a.name,a.salary,a.pin)

# Write a class “Calculator” capable of finding square, cube and square root of a number.

class calculator:

    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"the square of {self.n} is {self.n*self.n}")  
    
    def cube(self):
        print(f"the cube of {self.n} is {self.n*self.n*self.n}")  

    def sq_root(self):
        print(f"the square root of {self.n} is {self.n**1/2}")  

cal=calculator(4)
cal.square()
cal.cube()
cal.sq_root()