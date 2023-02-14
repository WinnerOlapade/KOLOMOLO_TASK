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
* “with” keyword helps to makes the code cleaner and more readable but more important use is to simplify file management by ensuring that files are always properly closed automatically when block is exited.



## Problem Solving
This *[folder](https://github.com/WinnerOlapade/KOLOMOLO_TASK/tree/master/problem_solving/)* contains corrected *[problem_solving.py](https://github.com/WinnerOlapade/KOLOMOLO_TASK/tree/master/problem_solving/problem_solving.py)* code
* Problem: File/code execution. the code refused to execute because the "if" statement in “line 41” ( `if __name__ == "main”:` ) wasn’t formatted properly.
  Solution: Correct format - ( `if __name__ == “__main__”:` ) to call main function correctly.

* Problem: AttributeError in line 17 (self.age == age) - the comparison operator (==) was used instead of assignment operator (=).
  Solution: Corrected to use the assignment “=“ operator.

* Problem: line 32 ( x = Person(p["first_name"], p["age"], p["last_name"]) ) the arguments were in the incorrect order. 
  Solution: Corrected to ( x = Person(p["first_name"], p["last_name"], p["age"]) ) to print the ages as integers.

* Problem: TypeError on line 25 ( `def increase_count()` ) increase_count definition needed a positional argument.
  Solution: Corrected to ( `def increase_count(self)` ).

* Added "for" statement in "main()" definition  
```
for thread in threads:
    thread.join()
``` 
to wait for thread to finish before proceeding so that "number of people created" is printed always at the very end.



## Create something whilst learning something new
Creating REST API in AWS using AWS API Gateway, Lambda and DynamoDB. This task (Infrastructure) was created using Terraform to allow easy deployment and management of resources in Cloud environment.

**Folder structure**
- [python_codes](https://github.com/WinnerOlapade/KOLOMOLO_TASK/tree/master/rest_api/)** contains 2 zipped files needed in the Terraform file *[main.tf](https://github.com/WinnerOlapade/KOLOMOLO_TASK/tree/master/rest_api/python_codes/)
- [main.tf](https://github.com/WinnerOlapade/KOLOMOLO_TASK/tree/master/rest_api/)** contains 2 zipped files needed in the Terraform file *[main.tf](https://github.com/WinnerOlapade/KOLOMOLO_TASK/tree/master/rest_api/main.tf)
- [get_function.zip](https://github.com/WinnerOlapade/KOLOMOLO_TASK/tree/master/rest_api/)** contains 2 zipped files needed in the Terraform file *[main.tf](https://github.com/WinnerOlapade/KOLOMOLO_TASK/tree/master/rest_api/get_function.zip)
- [post_function.zip](post_function.zip)

The Terraform folder **[REST_API](https://github.com/WinnerOlapade/KOLOMOLO_TASK/tree/master/rest_api/)** contains 2 zipped files needed in the Terraform file *[main.tf](https://github.com/WinnerOlapade/KOLOMOLO_TASK/tree/master/rest_api/main.tf)* having 2 variables "account_id" and "main_region", can be executed with `terraform apply` and then a subsequent "yes" reply when prompted.
    Executing the terraform file:
    - takes the variables and creates a DynamoDB Table named "users",
    - creates 2 Lambda functions (GET and POST), 
    - creates a IAM role with DynamoDB permissions and attaches the role to the lambda functions, 
    - creates a REST API Gateway with name "userManagement",
    - creates 2 API Gateway methods (GET and POST) and integrates the lambda functions to the corresponding API gateway methods. 
    - It also gives API permission to invoke the Lambda functions and, 
    - finally deploys the API getting back the output of GET and POST method urls.


### POST GET METHOD
> API POST Method URL: "https://qc9g7i6iyj.execute-api.us-east-1.amazonaws.com/v1/users"


**example body:**
```
'{"first_name":"John", "age":"32"}'
```

**Invocation**
```
curl -X POST -H "Content-Type: application/json" -d '{"first_name":"John", "age":"32"}' https://qc9g7i6iyj.execute-api.us-east-1.amazonaws.com/v1/users
```


#### API GET METHOD
> API GET Method URL: "https://qc9g7i6iyj.execute-api.us-east-1.amazonaws.com/v1/{user_id}"

To make a GET Request simply click link or copy and paste link in browser and edit 
`{user_id}` with "user id" from making a POST Request or random id (will return error) .



## Hanoi Towers
The Python programe [hanoi_towers.py](https://github.com/WinnerOlapade/KOLOMOLO_TASK/tree/master/programming_task/hanoi_towers.py) when executed will ask for input filename and reads the user input from the file, follow the moves and if at any point of the game the player either does an illegal move or solves the puzzle, the program prints the required message to console and exits.
