# [Python Review](https://www.youtube.com/watch?v=rfscVS0vtbw)

Table of Contents
=================

   * [Description](#description)
   * [Hello World](#hello-world)
   * [Print Shapes](#print-shapes)
   * [Variables](#variables)
   * [Strings](#strings)
      * [rendering literal characters](#rendering-literal-characters)
      * [printing a variable](#printing-a-variable)
      * [concatenation](#concatenation)
      * [lowercase function](#lowercase-function)
      * [uppercase function](#uppercase-function)
      * [check string is uppercase or lowercase](#check-string-is-uppercase-or-lowercase)
      * [nesting functions](#nesting-functions)
      * [string length](#string-length)
      * [indexing characters in a string](#indexing-characters-in-a-string)
      * [return the first index of a character](#return-the-first-index-of-a-character)
      * [replace characters within a string](#replace-characters-within-a-string)
      * [strings to decimal value](#strings-to-decimal-value)
      * [strings to integer value](#strings-to-integer-value)
   * [Numbers](#numbers)
      * [printing a number](#printing-a-number)
      * [printing decimals](#printing-decimals)
      * [printing negatives](#printing-negatives)
      * [adding numbers](#adding-numbers)
      * [subtracting numbers](#subtracting-numbers)
      * [multiplying numbers](#multiplying-numbers)
      * [dividing numbers](#dividing-numbers)
      * [remainders](#remainders)
      * [order of operations](#order-of-operations)
      * [integer variables](#integer-variables)
      * [float variables](#float-variables)
      * [converting numbers to string](#converting-numbers-to-string)
      * [absolute value](#absolute-value)
      * [exponents](#exponents)
      * [maximum of multiple numbers](#maximum-of-multiple-numbers)
      * [minimum of multiple numbers](#minimum-of-multiple-numbers)
      * [rounding a decimal to integer](#rounding-a-decimal-to-integer)
      * [importing more math functions](#importing-more-math-functions)
      * [rounding down a decimal value](#rounding-down-a-decimal-value)
      * [rounding up a decimal value](#rounding-up-a-decimal-value)
      * [square root](#square-root)
   * [Input](#input)
      * [recieve input](#recieve-input)
      * [storing input](#storing-input)
      * [math with input](#math-with-input)
      * [concatenating input](#concatenating-input)
   * [Lists](#lists)
      * [declaring a list](#declaring-a-list)
      * [indexing items in a list](#indexing-items-in-a-list)
      * [indexing from the back](#indexing-from-the-back)
      * [sublists](#sublists)
      * [modifying an item in a list](#modifying-an-item-in-a-list)
      * [appending lists](#appending-lists)
      * [inserting an item](#inserting-an-item)
      * [remove last item](#remove-last-item)
      * [find index of an item](#find-index-of-an-item)
      * [count instances of item](#count-instances-of-item)
      * [sorting](#sorting)
      * [reversing](#reversing)
      * [copying](#copying)
   * [Tuples](#tuples)
      * [declaring a tuple](#declaring-a-tuple)
      * [indexing items in a tuple](#indexing-items-in-a-tuple)
   * [Functions](#functions)
      * [defining a function](#defining-a-function)
      * [input parameters](#input-parameters)
      * [return](#return)
   * [If Statements](#if-statements)
      * [declaring if statements](#declaring-if-statements)
      * [or](#or)
      * [and](#and)
      * [not](#not)
      * [comparisons](#comparisons)
   * [Dictionaries](#dictionaries)
      * [declaring a dictionary](#declaring-a-dictionary)
      * [referencing keys](#referencing-keys)
      * [default value](#default-value)
   * [While Loops](#while-loops)
      * [declaring a while loop](#declaring-a-while-loop)
   * [For Loops](#for-loops)
      * [declaring a for loop](#declaring-a-for-loop)
   * [2D Lists](#2d-lists)
      * [declaring a 2D list](#declaring-a-2D-list)
      * [indexing items within a 2d list](#indexing-items-within-a-2d-list)
      * [iterate through each item in a 2D list](#iterate-through-each-item-in-a-2D-list)
   * [Commenting](#commenting)
      * [writing comments](#writing-comments)
   * [Try and Except](#try-and-except)
      * [declaring a try and accept block](#declaring-a-try-and-accept-block)
   * [Classes and Objects](#classes-and-objects)
      * [defining a class and objects](#defining-a-class-and-objects)
      * [using a class](#using-a-class)
      * [class functions](#class-functions)
      * [inheriting](#inheriting)


# Description

A review of basic python syntax based off of FreeCodeCamp's Youtube Tutorial. Within this repo, will mostly be code used during the [tutorial](https://www.youtube.com/watch?v=rfscVS0vtbw). The format of this document will also follow similarly to the time stamps.

# Hello World

```python
#generic hello world print statement
print("hello world")

```

# Print Shapes

```python
#generic triangle print statement
print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")
```

# Variables

```python
# with variables
character_age = "18"
character_name = "Van"

print("There was once a man named " + character_name + ", he was " + character_age)

# without variables
print("There was once a man named Van, he was 18")

# variable examples
string = "this is a string"
integer = 8
float_example = 2.0
boolean = True
```

# Strings

### rendering literal characters

```python
#rendering literal characters
print("this is a \"quote\" ")
```

### printing a variable

```python
#printing a variable
variable = "text"
print(variable)
```

### concatenation

```python
#concatenation
statement = "string"
print("this is a " + statement)

```

### lowercase function

```python
#lowercase function
lowercase_text = "THIS IS LOWERCASE"
print(lowercase_text.lower())
```

### uppercase function

```python
#uppercase function
uppercase_text = "this is uppercase"
print(uppercase_text.upper())
```

### check string is uppercase or lowercase

```python
#check string is uppercase or lowercase
check = "is this uppercase"
print(check.isupper())

print(check.islower())
```

### nesting functions

```python
#nesting functions, the code below is equivalent
item = "this is a item"
item_upper = item.upper()
print(item_upper.isupper())

print(item.upper().isupper())
```

### string length

```python
#string length
length = "what is this string length"
print(len(length))
```

### indexing characters in a string

```python
#indexing the first character
string_index = "index this string"
print(string_index[0])
```

### return the first index of a character

```python
#return the first index of a character
index_string = "index this string"
print(index_string.index("d"))
```

### replace characters within a string

```python
#replace characters within a string
replace_string = "replace this"
print(replace_string.replace("this", "that"))
```

### strings to decimal value

```python
#strings to decimal value
print(float("5"))
```

### strings to integer value

```python
#strings to integer value
print(int("5"))
```

# Numbers

### printing a number

```python
#printing a number
print(2)
```

### printing decimals

```python
#printing decimals
print(2.1189)
```

### printing negatives

```python
#printing negatives
print(-2)
```

### adding numbers

```python
#adding numbers
print(1 + 2)
```

### subtracting numbers

```python
#subtracting numbers
print(2 - 1)
```

### multiplying numbers

```python
#multiplying numbers
print(2 * 2)
```

### dividing numbers

```python
#dividing numbers
print(2 / 2)
```

### remainders

```python
#remainders
print(10 % 3)
```

### order of operations

```python
#python follows order of operations
print(2 * 3 + 4 - 1)
print(2 * (3 + 4 - 1))
```

### integer variables

```python
#integer variables
my_int = 5
```

### float variables

```python
#float variables
my_float = 5.0
```

### converting numbers to string

```python
#converting numbers to string
print(str(5) + " is a number")
```

### absolute value

```python
#absolute value
print(abs(-5))
```

### exponents

```python
#exponents, first integer is base and second is exponent
print(pow(3, 2))

```

### maximum of multiple numbers

```python
#maximum of multiple numbers
print(max(1, 2))
```

### minimum of multiple numbers

```python
#minimum of multiple numbers
print(min(1, 2))
```

### rounding a decimal to integer

```python
#rounding a decimal to integer
print(round(4.6))
```

### importing more math functions

```python
#importing more math functions
from math import *
```

### rounding down a decimal value

```python
#rounding down a decimal value
print(floor(2.9))
```

### rounding up a decimal value

```python
#rounding up a decimal value
print(ceil(2.1))
```

### square root

```python
#square root of a number as a decimal value
print(sqrt(9))
```

# Input

### recieve input

```python
#recieve input from user with a prompt, inputs are strings by defualt
input("this is your prompt: ")
```

### storing input

```python
#storing input to a variable
name = input("what is your name? ")
age = input("what is your age? ")
print("hello " + name +"!" + " You are " + age + " years old!")
```

### math with input

```python
#using math functions with input numbers
num_one = input("input first number: ")
num_two = input("input second number: ")

#accepts decimal numbers
result_float = float(num_one) + float(num_two)

#accepts only integers
result_int = int(num_one) + int(num_two)

print(result_float)
print(result_int)
```

### concatenating input

```python
#concatenating input variables with mad libs
first = input("input first word: ")
second = input("input second word: ")
third = input("input third word: ")

print("Roses are " + first)
print(second + " are blue")
print("I love " + third)
```

# Lists

### declaring a list

```python
#declaring a list
list = ["item", 3, True]
print(list)
```

### indexing items in a list

```python
#indexing the first item in a list, begins at 0
index_list = ["item", 3, True]
print(index_list[0])
```

### indexing from the back

```python
#indexing the first item from the back of a list, begins at -1
back_list = ["item", 3, True]
print(index_list[-1])
```

### sublists

```python
#indexing a sublist within a list, second number is non-inclusive
sub_list = ["item", 3, True]
print(sub_list[1:3])

#indexing a sublist beginning at a certain index
sub_list2 = ["item", 3, True]
print(sub_list2[1:])
```

### modifying an item in a list

```python
#modifying an item in a list
modify_list = ["first", "second", "third", "fourth", "fifth"]
modify_list[1] = "change"
print(modify_list)
```

### appending lists

```python
#appending lists
first_list = [1, 2, 3]
second_list = [4, 5, 6]
first_list.extend(second_list)
print(first_list)
```

### inserting an item

```python
#inserting an item into an index of the list
insert_list = [1, 2, 3, 4]
insert_list.insert(1, "insert")
print(insert_list)
```

### remove last item

```python
#remove last item in a list
pop_list = [1, 2, 3, 4]
pop_list.pop()
print(pop_list)
```

### find index of an item

```python
#find index of an item in the list
find_list = [1, 2, 3, 4]
print(find_list.index(3))
```

### count instances of item

```python
#count instances of item in list
count_list = [1, 1, 1, 2, 4]
print(count_list.count(1))
```

### sorting

```python
#sorting a list
sort_list = [1, 2, 4, 7, 5, 9, 8]
sort_list.sort()
print(sort_list)
```

### reversing

```python
#reversing a list
rev_list = [1, 2, 3, 4, 5]
rev_list.reverse()
print(rev_list)
```

### copying

```python
#copying a list
org_list = [1, 2, 3]
new_list = org_list.copy()
print(new_list)
```

# Tuples

### declaring a tuple

```python
#declaring a tuple, tuples are immutable
coordinates = (4, 5)
```

### indexing items in a tuple

```python
#indexing the first element in a tuple
index_tuple = (1, 2, 3, 4, 5)
print(index_tuple[0])
```

# Functions

### defining a function

```python
#defining a function
def function():
    print("this is my function")
```

### input parameters

```python
#defining a function with input parameters
def function_para(inputs):
    print("this is my function wiht a parameter of " + inputs)
```

### return

```python
#returning information from functions
def cube(num):
    return (num * num * num)
```

# If Statements

```python
#declaring if statements
condition = True
if condition:
    print("conditon is true")
else:
    print("conditon is not true")
```

### declaring if statements

```python
#declaring or conditonals
is_male = True
is_tall = False

if is_male or is_tall:
    print("they are male or tall or both")
else:
    print("they are neither male nor tall")
```

### or

```python
#declaring or conditonals
is_male = True
is_tall = False

if is_male or is_tall:
    print("they are male or tall or both")
else:
    print("they are neither male nor tall")
```

### and

```python
#declaring and conditionals
is_smart = False
is_short = True

if is_smart and is_short:
    print("you are smart and short")
else:
    print("you are not smart and short")
```

### not

```python
#declaring not conditionals
is_sick = False

if not(is_sick):
    print("you are not sick")
else:
    print("you are sick")
```

### comparisons

```python
#declaring comparisons
num1 = 1
num2 = 2

if num1 > num2:
    print("num1 is greater than num2")
else:
    print("num2 is greater than num1")
```

# Dictionaries

### declaring a dictionary

```python
#declaring a dictionary
dict = {
    "key": "value",
    "key2": "value2",
}
```

### referencing keys

```python
#referencing keys in a dictionary
ref = {
    "key": "value",
    "three": 3,
    "true": True, 
}

print(ref["key"])
print(ref.get("key"))
```

### default value

```python
#specify a default value for invalid key references
spec = {
    "key": "value",
    "three": 3,
    "true": True, 
}

print(spec.get("key here", "default message here"))
```

# While Loops

### declaring a while loop

```python
#declaring a while loop
condition = True

while condition:
    print("this code will run as long acondition is true!")
```

# For Loops

### declaring a for loop

```python
#declaring a for loop
list = ["item", "item", "item"]

for item in list:
    print("this code will run for every item in the list!")
```

# 2D Lists


### declaring a 2D list

```python
#declaring a 2D list
list_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

### indexing items within a 2d list

```python
#indexing the first item within a 2D list
index_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(index_list[0][0])
```

### iterate through each item in a 2D list

```python
#iterate through each item in a 2D list
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in grid:
    for col in row:
        print(col)
```

# Commenting

### writing comments

```python
#comments in python will have the "#" written in front of them
```

# Try and Except


### declaring a try and accept block

```python
#declaring a try and accept block
try:
    num = int(input("enter a string: "))
    print(num)
except:
    print("an error has occured!")
```

# Classes and Objects


### defining a class and objects

```python
#defining a class and object
class student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
```

### using a class

```python
#using a class
class student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

Alex = student("Alex", "Computer Science", 3.1)
```

### class functions

```python
#defining class functions
class student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

Alex = student("Alex", "Computer Science", 3.1)

print(Alex.on_honor_roll())
```

### inheriting

```python
#inheriting class information
class student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

class alumni(student):
    def is_attending(self):
        return False

Alex = alumni("Alex", "Computer Science", 3.1)

print(Alex.is_attending())  
```
