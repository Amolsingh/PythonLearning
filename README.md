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

# Functions
- Not all functions return a value. Some functions just do some action. Eg: print() and sort(). These functions don't return anything useful.
- A function thats bound to an instance of a class is called a method. Eg: String method str.casefold()
- You can use methods in the same way as you use functions but specify the object that they will act on, befor the dot.
- Function definition starts with a keyword **def**
     - Next name of the function
     - parameters for the function
- Use step into to debug inside the function
- The scope of variable used inside a function is limited inside function only. We can check this in the debug pane as the function variable disappear after function has performed its operation
- Arguments are the values that will be used by formal parameters, when we call a function.
- Python argument are passed by assignment.
- The behaviour is similar to pass by reference, when passing a mutable object. For immutable objects, the behaviour is closer to pass by value.
- When you define a function to have positional arguments, the argument are assigned to the parameters in their corresponding positions.
- If you want a function to return a value, use the return keyword to specify the value that should be returned
- Not all functions return something useful. Some functions perform an action, rather than producing a value.
- If you dont explicitly return a value, python will automatically return None
- It is valid to explicitly return None from your function. You might do that to indicate something wasn't found for example: The dictionary get method does this
- Function that perform an action, rather than returning a value, used to be called procedures. But that distinction is no longer made, in modern programming languages.
- We can raise error and handle scenarios using errors like ValueError, TypeError etc
- We can provide the default of the parameter in the function. Eg: **def calculate (x, y=3.14)**
- Documentation makes function easy to use and make it more intuitive to use
- Types of Parameters:
   - Positional or Keyword
   - Positional only
   - keyword only
   - var-positional
   - var-keyword
- Notice that the function docstrings are inside the functio definition
- The convention in C++ and Java is to put the docstrings before the function declaration
- In python, the docstrings go inside the function. There is a good reason for that. They become an attribute of the function.
- Remember that everything in Python is an object. That means functions can have attributes
- Each .py file that you create becomes a new Python module.
- Modules can be imported into other modules or executed 
- Python docstrings appear inside the function. They become an attribute of the function
      help(get_integer)
         - help(<name_ofmethod>)
      print(input.__doc__)
- Check your docstring by using ctrl + Q
- Any positional-or-keyword arguments that we defined, MUST come first in the parameter list
- If we have var-positional parameter thats a parameter that starts with * then it must come after any positional-or-keyword argument
- Any parameters defined after a var positional parameters must be keyword-only arguments (which includes var-keywords arguments)

# Function Annotations and Type hints
- def is_palindrome (String: tr) -> bool:
   return string[::-1].casefold() == string.casefold()
   
- Even though Python allows us to provide function annotations and gives us type hint we can still pass any type as Python is statically typed. The IDE only gives us the warning
- Docstrings can contain the error that a function may raise
      : raises ValueError:

# Python Environment
- A python virtual environment is an isolated installation of Python, separate from you main installation.
- If you had to update the pip & setup tools packages, you'll have seen that packages come in different versions. Python pacages get updated, just like anything else
- If you have a program that works with a particular version of package it might break when you update the package
- If you install new versions into your Python installation, you could break a program that you rely on
- A python virtual environment contains a copy of your main Python installation
- Bret Cannon is in the pannel of Python comittee
- The isolated environments we are using are virtualenvs. They are built into Python and the Jetbrains IDEs have good support for them
- Testing is the process of finding out if there are any bugs in your code
- Debugging is the process of working out what the bugs are, and fixing them 
- Testing and debugging go together
- You have to test the code first to find out if they have any bugs




