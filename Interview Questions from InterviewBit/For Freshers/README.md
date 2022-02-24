# Python Interview Questions for Freshers
## Q1. What is Python? What are the benefits of using Python?
> _Python is a high level, interpreted and general purpose language. Being a general purpose language, it can be used to almost any type of applications with the right tools and libraries. Additionaly, Python supports objects, modules, threads, exception handling and automatic memory management which help in modelling real-world problems and building applications to solve these problems._
<b><br>
> ***Benefits of using Python***
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
  
  | Class Name |  Description |
  | --- | --- |
  |  NoneType  |Represents the **NULL** values in Python| 
  
  
