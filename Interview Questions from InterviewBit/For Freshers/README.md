# Python Interview Questions for Freshers
## Q1. What is Python? What are the benefits of using Python?
> _Python is a high level, interpreted and general purpose language. Being a general purpose language, it can be used to almost any type of applications with the right tools and libraries. Additionaly, Python supports objects, modules, threads, exception handling and automatic memory management which help in modelling real-world problems and building applications to solve these problems._
<b><br>
> Benefits of using Python
> * Python is a general purpose programming language that has a simple, easy to learn syntax that emphasizes readability and therefore reduces the cost of programming maintenance. Moreover, the language is capable of scripting, it is also completely open source and supports third paty packages encouraging modularity and code reuse.
> * Its high-level data structures, combined with dynamic typing and dynamic binding, attract a huge community of developers for Rapid Application Development and deployment.
  
## Q2. What is Interpreted Language?   
> _An interpreted language execute it's statements line by line. Language such as Python, Javascript, R, PHP and Ruby are the examples of interpreted language. Programs written in an interpreted language runs directly from the source code, with no intermediary compilation step._
  
## Q3. What is PEP 8  and why it is important?
> _PEP stands for Pyhton Enhancement Proposal. A PEP is an official design document providing infromation to the Python Community, or describing a new feature for Python or it's process. PEP 8 is especially important since it documents the style guidelines for the Python code. Apparently contributing to the Python open source community requires you to follow these style guidelines sincerely and strictly._

## Q4. What is Scope in Python?
> _Every object in Python functions within a scope. A scope is a block of code where an object in Python reamins relevant. Namespaces uniquely identify all the objects identify all the objects inside a program. However, these namespaces also have a scope defined for them where you could use their objects without any prefix. A few examples of scope created during code execution in Python are as follows:_
<br><br>
> * A **local scope** refers to the local objects available in the current funciton.
> * A **global scope** refers to the objects available throughout the code execution since their inceprtion.
> * A **module level scope** refers to the global objects of the current module acccessible in the program.
> * An **outermost scope** refers to all the built-in names callable in the program. The object in this scope are searched last to find the name referenced.
```md
Note: Local scope objects can be synced with global scope objects using keywords such as global.
```
## Q5. What are the common built-in data types in Python?
> _There are several built-in data types in Python. Although, Pyhton doesn't require data types to be defined explicitly during variable declarations type errors are likely to occur if knowledge of data types and their compatability with each other are neglected. Pyhton provides **`type()`** and **`isinstance()`** functions to check the type of these variables. These types can be grouped into the following categories:_
<br><br>
> 1. None Type: <br>
> `None` keyword represents the null values in Python. Boolean equality operation can be performed using these NoneType objects.
  
>  | Class Name |  Description |
>  | --- | --- |
>  |  NoneType  |Represents the **NULL** values in Python| 
  
> 2. Numeric Types: <br>
  There are three different numeric types - **integers, floating-point numbers, and complex numbers.** Additionaly, booleans are a sub-type of integers.
  
>  | Class Name |  Description |
>  | --- | --- |
>  | int | Stores integer literals including hex, octal and binary numbers as integers |
>  | float | Stores literals containg decimal values and/or exponent signs as floating-point numbers |
>  | complex | Stores complex numbers in the form (A + Bi) and has attributes: `real` and `imag` |
>  | bool  | Stores boolean values (True or False) |

  `Note: The standard library also includes fractions to store rational numbers and decimals to store floating-point numbers with user defined precision.`

> 3. Sequence Types: <br>
  According to Python Documents, there are three basic Sequence Types - **list, tuples** and **range** objects. Sequence types have the `in` and `not in` operators defined for their travering their elements. These operators share the same priority as the comparison operations.
  
>  | Class Name  | Description |
>  | --- | --- |
>  | list  | Mutable sequence used to store the collection of items  |
>  | tuple | Immutable sequence used to store collection of items  |
>  | range | Represents an immutable sequence of numbers generated during execution  |
>  | str  |  Immutable sequence of Unicode code points to store textual data |
  
  ```md
  Note: The standard library also includes including additional types for processing:
  1.  Binary data such as bytearray bytes, memeoryview
  2.  Text strings such as str
  ```

> 4. Mapping Types: <br>
  A mapping object can map hashable values to random objects in Python. Mappings objects are mutable and there is currently only one standard mapping type, the **dictionary**.
  
>  | Class Name  | Description |
>  | --- | --- |
>  | dict  | Stores comma-separated list of key: value pairs |
 
> 5. Set Types: <br>
  Currently, Python has two built-in set values -**set** and **frozenset.** **Set** type is mutable and supports methods like `add()` and `remove()` **frozenset** tyoe is immutable and can't be modiifed after creation.
  
>  | Class Name  | Description |
>  | --- | --- |
>  | set | Mutable unorderd collection of distinct hashable objects  |
>  | frozenset | Immutable collection of distinct hashable objects |
  
> **NOTE:** `set` is mutable and thus cannot be used as key for a dictionary. On the other hand, `frozenset` is immutable and thus, hashable, and can be used as a dictionary key or as an element of another set.
  
> 6. Modules: <br>
  Module is an addditional built-in type supported by the Pyhton Intepreter. It supports one special operation, i.e., **attribute access:** `mymod.myobj`, where `mymod` is a module and `myobj` refrences a name defined in m's symbol table. The module's symbol table resides in a very special attribute of the module `_dict_`, but direct assignment to this module is neither possible nor recommended.
> 7. Callable Types: <br>
  Callable types are the types to which function call can be applied. They can be user-defined functions, instance methods, generator functions, and some other built-in functions, methods and classes.

##Q6. What is pass in python?
>The `pass` keyword represents a null operation in Python. It is generally used for the purpose of filling up empty blocks of code which may execute during runtime but has yet to be written.
