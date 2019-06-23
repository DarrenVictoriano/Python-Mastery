# Primitive Types

### Overview
Python has 4 primitive data structures:
* [Integer](#int)
* [Float](#float)
* [String](#str)
* [Boolean](#bool)

and 6 non-primitive data structures:
* [Arrays](#arr)
* [Lists](#list)
* [Tuples](#tuple)
* [Dictionary](#dict)
* [Sets](#set)
* [Files](#file)

___

# <span id="int">Intergers</span>

Just as in mathematics (where it is referred to as a signed integer) an integer is a whole number that could hold a zero, positive or negative value. This is how you would create various integers in Python:

```python
#positive number
number = 25

# negative number
negative_number = -23

zero = 0
```

To check the type of an object in Python, use the built-in `type()` function, just like in the lines of code below:

```python
number = 100000000000000000000000
print(type(number))

# output in Python 3 will be
<type 'int'>
```

# <span id="float">Floats</span>
Float represents real numbers, a data type that is used to define floating decimal points. These are some examples of float numbers in Python:

```python
decimal_number = 25.33

decimal_number_two = 45.2424
```

# <span id="str">Strings</span>

String represents a sequence of characters (text) inside double or single quotes. In Python, strings are immutable so once it's declared the value can't be changed, instead a new object is created e.g:
```python
first_string = "Hello"
second_string = first_string
print(first_string)
#returns 'Hello'

print(second_string)
#returns 'Hello'

#let's change first_string
first_string = "I have changed"
print(second_string)
'Hello'
```

# <span id="bool">Booleans</span>
Booleans are used to represent truth values with two constant objects True and False. The  built-in function for converting an object to Boolean is `bool()`, e.g:

```python
num = 1
print(bool(num))
#returns True since Boolean in numeric can be present as 0 or 1
```

# <span id="arr">Array</span>
First off, arrays in Python are a compact way of collecting basic data types, all the entries in an array must be of the same data type. However, arrays are not all that popular in Python, unlike the other programming languages such as C++ or Java.

In general, when people talk of arrays in Python, they are actually referring to lists. However, there is a fundamental difference between them and you will see this in a bit. For Python, arrays can be seen as a more efficient way of storing a certain kind of list. This type of list has elements of the same data type, though.

In Python, arrays are supported by the `array` module and need to be imported before you start inititalizing and using them. The elements stored in an array are constrained in their data type. The data type is specififed during the array creation and specified using a type code, which is a single character like the `I` you see in the example below:

```python
import array as arr
a = arr.array("I",[3,6,9])
type(a)
# result
array.array
```

[Python Array documentation][arraydocs] page provides more information about the various type codes available and the functionalities provided by the `array` module.

[arraydocs]:https://docs.python.org/3/library/array.html

# <span id="list">List</span>
Lists in Python are used to store collection of heterogeneous items. These are mutable, which means that you can change their content without changing their identity. You can recognize lists by their square brackets `[` and `]` that hold elements, separated by a comma `,`. Lists are built into Python: you do not need to invoke them separately.

```python
x = [] # Empty list
type(x)
# list

x1 = [1,2,3]
type(x1)
# list

x2 = list([1,'apple',3])
type(x2)
# list

print(x2[1])
# apple

x2[1] = 'orange'
print(x2)
# [1, 'orange', 3]
```

# <span id="tuple">Tuples</span>
Tuples are another standard sequence data type. The difference between tuples and list is that tuples are immutable, which means once defined you cannot delete, add or edit any values inside it. This might be useful in situations where you might to pass the control to someone else but you do not want them to manipulate data in your collection, but rather maybe just see them or perform operations separately in a copy of the data.

Let's see how tuples are implemented:

```python
x_tuple = 1,2,3,4,5
y_tuple = ('c','a','k','e')
x_tuple[0]
1
y_tuple[3]
x_tuple[0] = 0 # Cannot change values inside a tuple

'''
---------------------------------------------------------------------

TypeError                Traceback (most recent call last)

<ipython-input-74-b5d6da8c1297> in <module>()
      1 y_tuple[3]
----> 2 x_tuple[0] = 0 # Cannot change values inside a tuple


TypeError: 'tuple' object does not support item assignment
'''
```

# <span id="dict">Dictionary</span>

Dictionaries are exactly what you need if you want to implement something similar to a telephone book. None of the data structures that you have seen before are suitable for a telephone book.

This is when a dictionary can come in handy. Dictionaries are made up of key-value pairs. key is used to identify the item and the value holds as the name suggests, the value of the item.

```python
x_dict = {'Edward':1, 'Jorge':2, 'Prem':3, 'Joe':4}
del x_dict['Joe']
x_dict

# {'Edward': 1, 'Jorge': 2, 'Prem': 3}
x_dict['Edward'] # Prints the value stored with the key 'Edward'.
1
```
You can apply many other inbuilt functionalies on dictionaries:

```python
len(x_dict)
# 3
x_dict.keys()
dict_keys(['Prem', 'Edward', 'Jorge'])
x_dict.values()
dict_values([3, 1, 2])
```
# <span id="set">Set</span>

Sets are a collection of distinct (unique) objects. These are useful to create lists that only hold unique values in the dataset. It is an unordered collection but a mutable one, this is very helpful when going through a huge dataset.

```python
x_set = set('CAKE&COKE')
y_set = set('COOKIE')

print(x_set)
{'A', '&', 'O', 'E', 'C', 'K'}
print(y_set) # Single unique 'o'
{'I', 'O', 'E', 'C', 'K'}
print(x - y) # All the elements in x_set but not in y_set

'''
---------------------------------------------------------------------

NameError                      Traceback (most recent call last)

<ipython-input-3-31abf5d98454> in <module>()
----> 1 print(x - y) # All the elements in x_set but not in y_set

NameError: name 'x' is not defined
'''

print(x_set|y_set) # Unique elements in x_set or y_set or both
{'C', '&', 'E', 'A', 'O', 'K', 'I'}
print(x_set & y_set) # Elements in both x_set and y_set
{'O', 'E', 'K', 'C'}
```

# <span id="file"> Files </span>

Files are traditionally a part of data structures. And although big data is commonplace in the data science industry, a programming language without the capability to store and retrieve previously stored information would hardly be useful. You still have to make use of the all the data sitting in files across databases and you will learn how to do this.

The syntax to read and write files in Python is similar to other programming languages but a lot easier to handle. Here are some of the basic functions that will help you to work with files using Python:

* `open()` to open files in your system, the filename is the name of the file to be opened;
* `read()` to read entire files;
* `readline()` to read one line at a time;
* `write()` to write a string to a file, and return the number of characters written; And
* `close()` to close the file.

```python
# File modes (2nd argument): 'r'(read), 'w'(write), 'a'(appending), 'r+'(both reading and writing)
f = open('file_name', 'w')

# Reads entire file
f.read()

# Reads one line at a time
f.readline()

# Writes the string to the file, returning the number of char written
f.write('Add this line.')

f.close()
```

The second argument in the open() function is the file mode. It allows you to specify whether you want to read (r), write (w), append (a) or both read and write (r+).

___
References:

* [Primitive Data Types in Python 3](https://able.bio/ZoranPandovski/primitive-data-types-in-python-3--57tqcfp) by Zoran Pandovski

* [Python Data Structures Tutorial](https://www.datacamp.com/community/tutorials/data-structures-python#primitive) by Sejal Jaiswal