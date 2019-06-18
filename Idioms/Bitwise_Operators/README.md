# Bitwise Operator

### Overview

Bitwise operators are operators that operates on binary level.
```
& (bitwise AND)
| (bitwise OR)
~ (bitwise NOT)
^ (bitwise XOR)
<< (bitwise left shift)
>> (bitwise right shift)
>>> (bitwise unsigned right shift)
&= (bitwise AND assignment)
|= (bitwise OR assignment)
^= (bitwise XOR assignment)
<<= (bitwise left shift and assignment)
>>= (bitwise right shift and assignment)
>>>= (bitwise unsigned right shift and assignment)
```

___

## The & Operator
A quick heads-up though: normally, `ints` and `uints` take up 4 bytes or 32 bits of space. This means each int or uint is stored as 32 binary digits. For the sake of this tutorial, we'll pretend sometimes that `ints` and `uints` only take up 1 byte and only have 8 binary digits.

The & operator compares each binary digit of two integers and returns a new integer, with a 1 wherever both numbers had a 1 and a 0 anywhere else. A diagram is worth a thousand words, so here's one to clear things up. It represents doing `37 & 23`, which equals `5`.

![example](./imgs/and_example.png)

Notice how each binary digit of 37 and 23 are compared, and the result has a 1 wherever both 37 and 23 had a 1, and the result has a 0 otherwise.
___

### References:
[Understanding Bitwise Operators](https://code.tutsplus.com/articles/understanding-bitwise-operators--active-11301) by Jason Killian