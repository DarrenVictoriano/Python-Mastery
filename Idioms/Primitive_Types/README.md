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

# <a id="int">Intergers</a>
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

# <a id="float">Floats</a>
Float represents real numbers, a data type that is used to define floating decimal points. These are some examples of float numbers in Python:

```python
decimal_number = 25.33

decimal_number_two = 45.2424
```

# <a id="str">Strings</a>

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

# <a id="bool">Booleans</a>
Booleans are used to represent truth values with two constant objects True and False. The  built-in function for converting an object to Boolean is `bool()`, e.g:

```python
num = 1
print(bool(num))
#returns True since Boolean in numeric can be present as 0 or 1
```

# <a id="arr">Array</a>
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

___
References:

* [Primitive Data Types in Python 3](https://able.bio/ZoranPandovski/primitive-data-types-in-python-3--57tqcfp) by Zoran Pandovski

* [Python Data Structures Tutorial](https://www.datacamp.com/community/tutorials/data-structures-python#primitive) by Sejal Jaiswal