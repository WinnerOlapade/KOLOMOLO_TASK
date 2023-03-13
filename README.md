# Solution to Tasks
This repository contains the solution to tasks given by Kolomolo

## Basic Knowledge
* `__main__.py` is used to specify entry point at which a program executes when packages or modules are executed as scripts. when a package or module is run as the main program using the python interpreter, `__mian__.py` file executes and serves as the starting point for the program. It allows for the code in the package or module to be executed as a standalone application rather than just a library.

* To prevent code in module from being execute when imported, wrap the code (if `__name__ == “__main__”:` ) block into the function. Setting this means the module will be executed only when its is executed as main program not when imported.

` __init__()` method is the method that represents a class constructor in Python

* ".string format method," "comma method," "f-string method," "% format method" are options used to insert vale of a variable into a string.

* Access can be restricted to a private method by marking it private which means adding “__” prefix to its name. However, python doesn’t really enforce privacy it is rather treated as private and is not accessible directly from outside the class. Private methods can still be accessed by using name mangling ("_MyClass__my_private_method").

Decorators can be used to add functionality to an existing function without modifying its source code. A decorator is a function that takes another function as input and returns a new function that adds some functionality to the original function. The decorator is applied to the original function using the "@my_decorator" syntax.

* @staticmethod is used to define a method that does not depend on the state of the class or instance. It is essentially a regular function that happens to be defined within a class. Because it does not depend on the state of the class or instance, it does not take any special parameters (e.g., self or cls). Instead, it takes only the arguments that are passed to it.
@classmethod, on the other hand, is used to define a method that operates on the class itself rather than on instances of the class. It takes a special first argument conventionally named cls, which refers to the class object itself. This allows the method to access and modify the class's attributes or call other class methods.

* `with` keyword is a context manager used in exception handling. Mostly used to simplify file management by ensuring that files are always properly closed automatically when block is exited. When reading or Writing a file in python it ensure that the file stream process doesn’t block other processes if an exception is raised, but terminates properly.
