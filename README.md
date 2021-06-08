# PythonLearning
Python has several built-in data types, that can be classed as:
 * numeric
 * iterator
 * sequence(Which are also Iterators)
 * mapping
 * file
 * class
 * exception

Python 3 has 3 numeric data types:
 * int : whole number does not having a fractional part
 * float : They have the fractional part
 * complex - They have real and imaginary part
 * Python int effectively has no maximum size. You will run out of memory before you exceed the size because there isnt any limit on the size
 * The maximum float value on a 64 bit computer is 1.7976931348623157e+308 which means move the decimal point 308 places right
 * The smallest float is 2.2250738585072014e-308, which has 307 zeroes before the decimal point.

Python 3 has 5 sequence types built in:
 * The String type
 * list
 * tuple
 * range
 * bytes and bytearray

A sequence is defined as the ordered set of items. For example, the word "HELLO WORLD" contains 11 items, and each item is a character.

A list is also a sequence type. For example, here's a Python list of things you might need, when buying a new computer
["computer", "monitor", "keyboard", "mouse", "mouse mat"]

Python provides Several ways to repeat a block of code - things like:
 * For Loops
 * while loops
 * list comprehensions and generator expressions

A for loop works by iterating over some set of values. It assigns each of values, one by one, to one or more variables
It then executes a block of code once for each value.

The set of values comes from a sequence, or some other iterable object

An iterable object is anything that can be iterated over. That means a sequence is also an iterable

Range is iterable

Remember how string slices returned the characters up to but not including the end number.
Ranges work in the same way. The last value specified is not included.

Python provides two main ways to loop round a block of code: for loops and while loops
 * For loops can be used to iterate over an iterable. 
 * Sometimes we need to keep looping as long as some condition is Trueand stop when it becomes false. We do this using While loop

A PEP is a python enhancement proposal
 * All changes and new features to the python language start with a proposal
 * The proposal is reviewed, discussed, improved if necessary, then either accepted or rejected
 * Untill 2018, Guido van Rossum made the final decision about whether to implement a PEP or not
 * Since then, the decision is taken by a group of people

# Conditional Debugging 
This can be used when we want the debugger to stop at a breakpoint when a specific condition is met
Simply right click over the breakpoint and give the condition on which you want to stop the debugger

# Sequence Types
* List
* Tuple
* Range

A sequence is a ordered collection of items
The word ordered here is important
* If a sequence wasnt ordered, you couldn't refer to individual
* items by their index position

In python anything that you can iterate over is an iterable. That means
if you can use it in a for loop then its iterable
* Iterable is an object that contains either __iter__ method or __getitem__ method
* Indexing must also start from 0

All sequence types can be iterated over
That means all sequence types - Strings, Lists, etc are also iterable types
Not all iterable are sequences
For example, you can use a dictionary in a for loop, but its not a sequence

String and List are both immutable, which means they cant be changed
Lists on the other hand are mutable. You can change the contents of a list

Immutable Ojects (cant be changed)
* int
* float
* bool
* str
* tuple
* frozenset
* bytes


A mutable object is one whose value can be changed
Python has the following mutable objects built in:
    * list
    * dict
    * set
    * Bytearray

We can change the value of the mutable objects, without the object being destroyed and re-created

# Built in functions
* len()
* int()
* str()
* input()
* print()
* sum()
* sorted()
* sort()


# Tuple

- Mathematical name for ordered set of data
- Ordered is a requirement for python sequence
- In python tuples are another sequence types along with strings, lists and ranges
- Tuples differ from list because tuples are immutable that means they cannot be changed after they are created. Just like strings.
- The main difference between a tuple and list if that Tuples are immutable
- Because they dont have the overhead of the methods needed to change them, tuples use less memory than lists. Thats one reason why you might want to use tuples
- If yu program is dealing with millions of these things, you can save memory by using a tuple
- Helps in protecting the integrity of your data as we cannot change the data once assigned.
- Using a List method we can convert a Tuple to a list

